<div align="center">
  <img src="assets/project-hero.svg" width="100%" alt="Smoking and Health Data Analysis" />
</div>

# Smoking & Health Data Analysis

건강검진 데이터에서 흡연자와 비흡연자의 건강 지표 차이를 살펴본 데이터 분석 프로젝트입니다. **7,000건, 18개 컬럼**을 대상으로 BMI, 충치, 중성지방, 혈압을 중심으로 분포와 관계를 비교했습니다.

## 분석 결과

| 항목 | 비흡연 | 흡연 | 관찰 결과 |
|---|---:|---:|---|
| 중성지방 평균 | 113.45 | **150.40** | 흡연자 집단이 높음 |
| 중성지방 중앙값 | 97 | **131** | 흡연자 집단이 높음 |
| 충치 있음 | 19.6% | **28.2%** | 흡연자 집단이 높음 |
| BMI 평균 | 23.81 | **24.73** | 흡연자 집단이 조금 높음 |
| 혈압 평균 | 45.42 | 45.76 | 큰 차이가 보이지 않음 |

BMI 구간별 흡연자 비율은 정상 `30.6%` → 비만전단계 `39.6%` → 1단계 비만 `41.8%` → 2단계 비만 `46.0%`로 높아지는 흐름이 관찰됐습니다. 3단계 비만은 흡연자 비율이 `43.9%`였지만 표본이 41명으로 작아 추세 해석에서 제외했습니다.

<p align="center">
  <img src="assets/cell_32_output_02.png" width="760" alt="BMI 구간별 흡연 여부 비율" />
</p>

흡연자 집단의 충치 발생 비율은 `28.2%`, 비흡연자 집단은 `19.6%`였습니다.

<p align="center">
  <img src="assets/cell_32_output_05.png" width="620" alt="흡연 여부별 충치 발생 비율" />
</p>

흡연 여부와의 Pearson 상관계수는 중성지방 `0.25`, BMI `0.13`, 충치 `0.10`, 혈압 `0.02`였습니다. 이번 분석에서 가장 뚜렷한 차이는 중성지방에서 확인됐습니다.

<p align="center">
  <img src="assets/cell_35_output_00.png" width="620" alt="흡연 여부와 건강 지표 간 상관관계" />
</p>

## 데이터와 전처리

흡연 여부 분포는 비흡연 4,429명(`63.27%`), 흡연 2,571명(`36.73%`)입니다. BMI와 나이는 구간형 파생변수로 만들었고, 결측값은 변수 특성에 따라 처리했습니다.

| 변수 | 결측치 | 처리 방법 |
|---|---:|---|
| 혈압 | 140 | 중앙값 |
| 시력 | 140 | 최빈값 |
| 중성지방 | 140 | 연령대별 평균, 이후 남은 값은 전체 평균 |
| 공복 혈당 | 140 | 전체 평균 |

분석 환경은 Python과 `pandas`, `numpy`, `matplotlib`, `seaborn`입니다. 필요한 패키지는 [`requirements.txt`](requirements.txt)에 정리되어 있습니다.

## 해석 범위

이 결과는 관찰 데이터에서 확인한 **집단 차이와 상관관계**입니다. 흡연이 특정 건강 지표의 변화를 직접 일으켰다는 인과관계로 해석하지 않습니다.

발표에서는 혈압 데이터의 성격, 성별 정보 부재, 흡연 여부와 연령대의 표본 불균형, 생활 습관 변수 부재를 주요 한계로 정리했습니다.

## Repository

```text
smoking_health_data/
├── README.md
├── LICENSE
├── CONTRIBUTORS.md
├── requirements.txt
└── assets/
    ├── project-hero.svg
    └── 분석 결과 시각화
```

원본 건강검진 데이터는 공개 저장소에 포함하지 않습니다.

## Team

**김진형 · 남한솔 · 안상균 · 이희진**  
OZ Coding School · 11조 헬스 케어 동아리  
[`CONTRIBUTORS.md`](CONTRIBUTORS.md)

Organization: [`oz-dongari`](https://github.com/oz-dongari)

## License

**All Rights Reserved.** 복제·수정·배포·재사용에는 저작권자 사전 허가가 필요합니다. [`LICENSE`](LICENSE)
