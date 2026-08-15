<div align="center">
  <img src="assets/project-hero.svg" width="100%" alt="Smoking and Health Data Analysis" />
</div>

# Smoking & Health Data Analysis

건강검진 데이터 **7,000건 · 18개 컬럼** 기반 흡연 여부별 건강 지표 분석  
주요 지표: BMI · 충치 · 중성지방 · 혈압

## 분석 결과

| 항목 | 비흡연 | 흡연 | 관찰 결과 |
|---|---:|---:|---|
| 중성지방 평균 | 113.45 | **150.40** | 흡연자 집단이 높음 |
| 중성지방 중앙값 | 97 | **131** | 흡연자 집단이 높음 |
| 충치 있음 | 19.6% | **28.2%** | 흡연자 집단이 높음 |
| BMI 평균 | 23.81 | **24.73** | 흡연자 집단이 조금 높음 |
| 혈압 평균 | 45.42 | 45.76 | 큰 차이 없음 |

**BMI 구간별 흡연자 비율**  
정상 `30.6%` → 비만전단계 `39.6%` → 1단계 비만 `41.8%` → 2단계 비만 `46.0%`  
3단계 비만 `43.9%` (`n=41`) — 소표본으로 추세 해석 제외

<p align="center">
  <img src="assets/cell_32_output_02.png" width="760" alt="BMI 구간별 흡연 여부 비율" />
</p>

**충치 있음 비율:** 비흡연 `19.6%` · 흡연 `28.2%`

<p align="center">
  <img src="assets/cell_32_output_05.png" width="620" alt="흡연 여부별 충치 발생 비율" />
</p>

**Pearson r:** 중성지방 `0.25` · BMI `0.13` · 충치 `0.10` · 혈압 `0.02`  
최대 절대값: 중성지방 `0.25`

<p align="center">
  <img src="assets/cell_35_output_00.png" width="620" alt="흡연 여부와 건강 지표 간 상관관계" />
</p>

## 데이터와 전처리

**흡연 여부:** 비흡연 4,429명 (`63.27%`) · 흡연 2,571명 (`36.73%`)  
**파생변수:** BMI 구간 · 연령대 구간

| 변수 | 결측치 | 처리 방법 |
|---|---:|---|
| 혈압 | 140 | 중앙값 |
| 시력 | 140 | 최빈값 |
| 중성지방 | 140 | 연령대별 평균, 이후 남은 값은 전체 평균 |
| 공복 혈당 | 140 | 전체 평균 |

**환경:** Python · `pandas` · `numpy` · `matplotlib` · `seaborn`  
패키지: [`requirements.txt`](requirements.txt)

## 해석 범위

관찰 데이터의 집단 차이·상관관계. 인과 추론 제외.

**주요 한계:** 혈압 변수 성격 · 성별 정보 부재 · 흡연 여부/연령대 표본 불균형 · 생활 습관 변수 부재

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

원본 건강검진 데이터 미포함

## Team

**김진형 · 남한솔 · 안상균 · 이희진**  
OZ Coding School · 11조 헬스 케어 동아리  
[`CONTRIBUTORS.md`](CONTRIBUTORS.md)

Organization: [`oz-dongari`](https://github.com/oz-dongari)

## License

**All Rights Reserved.** 복제·수정·배포·재사용은 저작권자 사전 허가 필요. [`LICENSE`](LICENSE)
