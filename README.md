# kaggle
# 📊 캐글 프로젝트


<img src="https://github.com/user-attachments/assets/5ecea204-59f6-4500-90ea-24e3b4d83e2b" alt="딥러닝발표자료" width="500">\

# 🗂 발표 자료
- [📂 발표자료 PDF](https://github.com/user-attachments/files/18146579/default.pdf)

# 📖 프로젝트 소개

이 프로젝트는 다양한 시계열 분석 모델과 머신러닝 기법을 활용하여 **매장 매출 시계열 데이터를 분석하고 예측**하는 시스템을 개발한 팀 프로젝트입니다. 본 프로젝트는 데이터 기반 예측을 통해 매출 변동성을 줄이고, 효율적인 재고 관리를 지원하는 것을 목표로 했습니다.

---

## 📂 프로젝트 주요 내용

### 1️⃣ **프로젝트 목표 및 필요성**
- 매장 매출 데이터를 분석하여 **효율적인 재고 관리**와 **고객 만족도 향상**.
- 과잉 재고로 인한 비용 증가 및 품절 문제 해결을 위해 시계열 분석 적용.
- **계절성, 추세성, 잔차**를 고려한 정밀한 예측 모델 구축.

### 2️⃣ **데이터 수집 및 전처리**
- 데이터 출처:
  - Kaggle: 매장 매출, 거래, 휴일 이벤트 데이터
  - Stores.csv: 매장 클러스터 및 특성 정보
  - Oil.csv: 유가 변동 데이터
- 주요 전처리 과정:
  - 결측치 보완: 유가 데이터의 공백을 보간법으로 처리
  - 데이터 병합: 거래 데이터와 휴일, 매장 특성을 결합
  - 정상성 검정 및 차분: 시계열 데이터의 정상성을 확보하기 위한 ADF, KPSS 테스트

### 3️⃣ **모델링 및 시도된 기법**
- **활용 모델**:
  - Python의 XGBoost, LightGBM, ARIMA, SARIMA
- **시도 모델**:
  - LSTM, GRU, Facebook Prophet
- **모델 평가 지표**:
  - RMSE, RMSLE, MAE, MAPE 등 다양한 성능 평가 지표 활용

### 4️⃣ **GPU 환경 구성**
- **사용된 하드웨어 및 소프트웨어**:
  - GPU: NVIDIA GTX 1080
  - CUDA 11.7 및 cuDNN 8.5
  - Python 기반 딥러닝 프레임워크: PyTorch, TensorFlow
- **최적화**:
  - 배치 크기 조정 및 Adam 옵티마이저 적용
  - 학습 시간 약 70% 단축

### 5️⃣ **결과 및 성과**
- **계절성 탐색 및 예측**:
  - 월별, 주별 계절성 분석 및 Power Spectral Density와 푸리에 변환으로 숨겨진 주기성 파악
  - ARIMA, SARIMA 모델로 안정적인 예측 성능 달성
- **앙상블 모델의 성과**:
  - LightGBM, XGBoost 모델이 우수한 RMSLE 기록
  - LightGBM 모델이 데이터 처리 효율성과 안정적인 성능 면에서 최적

---

# 🛠️ 사용된 기술 스택

### **Programming Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### **Libraries and Frameworks**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-007D9C?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-AA4C2C?style=for-the-badge)
![Mediapipe](https://img.shields.io/badge/Mediapipe-009688?style=for-the-badge&logo=mediapipe&logoColor=white)

### **Visualization Tools**
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)

---

# 📊 주요 성과
- **매장 매출 예측 정확도**:
  - XGBoost, LightGBM을 활용한 예측에서 높은 정확도 달성
  - LSTM, GRU 시도 결과 ARIMA/SARIMA 대비 낮은 성과
- **실제 적용 가능성**:
  - 계절성과 이벤트 특성을 반영하여 효율적인 재고 및 매출 관리 가능

---

# 🔗 참고 및 다음 단계
- 자세한 내용은 상단 발표자료 PDF 링크에서 확인 가능합니다.



