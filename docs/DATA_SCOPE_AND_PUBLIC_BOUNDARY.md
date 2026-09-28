# Data Scope and Public Boundary

이 문서는 `oz-dongari/smoking_health_data`의 데이터 해석 범위와 공개 저장소 경계를 명확히 하기 위한 기준 문서입니다.

## Data scope

- **Project:** OZ Coding School · AI Healthcare Mini Project · Team 11
- **Rows / columns used in the project:** 7,000 rows · 18 columns
- **Task in this repository:** 흡연 여부에 따른 건강 지표의 전처리 · 탐색적 데이터 분석(EDA) · 집단 비교 · 상관관계 시각화
- **Source boundary:** 프로젝트 과정에서 제공된 교육용 분석 데이터를 사용했습니다.
- **Not independently verified here:** 원본 수집기관, 실제 임상 측정 프로토콜, 모집단 대표성, 재사용·재배포 권리의 전체 범위

따라서 이 저장소는 데이터셋의 수치를 실제 임상 모집단의 기준값으로 일반화하지 않습니다.

## Blood-pressure variable caution

데이터셋의 `혈압` 변수는 평균이 약 45 수준으로 나타납니다.

이 값은 일반적인 임상 혈압 표기와 직접 대응한다고 확인할 근거가 이 저장소에 없으므로:

- 실제 수축기/이완기 혈압(mmHg)로 단정하지 않음
- 임상적 정상/비정상 기준과 직접 비교하지 않음
- 흡연 여부와의 관계도 **해당 데이터셋 내부 변수의 관찰적 차이**로만 해석

따라서 README의 혈압 수치는 `데이터셋 혈압 변수`로 표기합니다.

## Interpretation boundary

이 프로젝트는 관찰 데이터의 기술통계와 EDA입니다.

- 집단 평균 차이 ≠ 인과효과
- Pearson correlation ≠ 인과관계
- 낮은 표본 수의 구간은 추세 판단에서 제외
- 성별·생활습관 등 주요 교란요인이 데이터에 없으므로 외부 일반화를 제한
- 별도의 임상 검증, 진단 성능 검증, 의료 의사결정 성능을 주장하지 않음

## Public repository boundary

현재 default branch에는 원본 건강검진 CSV/XLSX/Parquet 파일을 포함하지 않습니다.

공개 저장소에는 다음만 유지합니다.

- 요약 통계
- 집계 비율
- 상관계수
- 시각화 이미지
- 분석 방법과 한계
- 팀/라이선스 문서

초기 Git history에는 분석 과정에서 생성된 row-level preview가 포함된 과거 문서 버전이 존재합니다. 현재 default branch에서는 해당 preview를 제거했으며, Git history 자체는 provenance 보존을 위해 재작성하지 않았습니다.

데이터 제공 조건이 과거 Git 객체까지 완전 삭제하도록 요구하는 경우에만 별도 history rewrite를 검토해야 합니다.

## Repository guard

`.github/workflows/public-data-boundary.yml`은 이후 변경에서 다음을 검사합니다.

- raw CSV/XLSX/Parquet 파일의 공개 커밋 방지
- 공개 Notebook 실행 output / execution count 방지
- text 파일에 row-level train/test ID preview가 다시 들어오는 것을 방지

이 guard는 데이터 라이선스를 대신 판단하지 않으며, default branch 공개 경계를 유지하기 위한 기술적 방어선입니다.


## CI status

Default branch changes are checked by `.github/workflows/public-data-boundary.yml`.  
The check is intended to fail closed if raw tabular files, row-level train/test ID previews, or executed Notebook outputs are committed.
