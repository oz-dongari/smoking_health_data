from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAW_DATA_SUFFIXES = {".csv", ".xlsx", ".xls", ".parquet"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yml", ".yaml"}
ROW_ID_PATTERN = re.compile(r"\b(?:TRAIN|TEST)_\d{4,}\b")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue

        rel = path.relative_to(root)

        if path.suffix.lower() in RAW_DATA_SUFFIXES:
            failures.append(f"raw tabular data file must not be committed: {rel}")
            continue

        if path.suffix.lower() == ".ipynb":
            try:
                notebook = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                failures.append(f"invalid notebook JSON: {rel} ({exc})")
                continue

            for index, cell in enumerate(notebook.get("cells", [])):
                if cell.get("cell_type") != "code":
                    continue
                outputs = cell.get("outputs", [])
                if outputs:
                    failures.append(
                        f"notebook output must be cleared: {rel} cell {index} "
                        f"({len(outputs)} output item(s))"
                    )
                if cell.get("execution_count") is not None:
                    failures.append(f"execution_count must be null: {rel} cell {index}")
            continue

        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if ROW_ID_PATTERN.search(text):
                failures.append(f"row-level train/test ID preview detected: {rel}")

    if failures:
        print("Public data boundary check FAILED:")
        for item in failures:
            print(f"- {item}")
        return 1

    print(
        "Public data boundary check passed: no raw tabular data files, "
        "no row-level train/test ID previews, and no executed notebook outputs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
