# kaggle
# 🏋️‍♂️ 딥러닝 기반 운동 자세 평가 및 분류 프로젝트


<img src="https://github.com/user-attachments/assets/69cc6311-c11d-46eb-8d59-10b60dffaa92" alt="딥러닝발표자료" width="500">\

---
## 🗂 발표 자료
- [📂 발표자료 PDF](https://github.com/tjehdgus/deep_learning/blob/main/%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf)
- 프로젝트의 자세한 내용은 발표자료에서 확인할 수 있습니다:  
## 📖 프로젝트 소개

이 프로젝트는 Mediapipe와 TSM 기반 딥러닝 모델을 활용하여 **운동 자세를 분류하고 평가**하는 시스템을 개발한 팀 프로젝트입니다. 본 프로젝트는 다양한 운동 자세를 평가하여 정확도를 개선하고, 사용자 맞춤형 피드백을 제공하는 것을 목표로 했습니다.

---

## 📂 프로젝트 주요 내용

### 1️⃣ **주제 선정**
- 현대인의 운동 부족 문제 해결을 목표로 프로젝트 기획.
- **비만율 통계**와 **헬스 이용객 통계**를 분석하여 운동 자세의 중요성을 확인.

### 2️⃣ **데이터 수집**
- **AI Hub**: 운동 자세 이미지 데이터
- **KOSIS 국가통계포털**: 비만율 및 헬스 이용객 통계
- **네이버 블로그 크롤링**: 운동 관련 감정 분석 데이터
- **데이터 포맷**: JSON 형태로 좌표 및 운동 상태를 저장 (2D, 3D 좌표 포함)

### 3️⃣ **모델 생성**
- **TSM(Temporal Shift Module) 기반 딥러닝 모델**:
  - 시간적 특성과 공간적 정보를 학습하여 운동 자세를 분류.
  - Confusion Matrix, ROC Curve, Precision, Recall, F1-Score로 성능 평가.

### 4️⃣ **Mediapipe 활용**
- **운동 관절 추적**:
  - Mediapipe로 관절 좌표를 추출 후, **운동 분류 및 자세 평가**.
  - 추가로 Neck(목), Pelvis(골반), Spine(척추)의 좌표를 계산하여 자세 정밀도 향상.

### 5️⃣ **모델 및 시연영상 구현**
- TSM 모델로 운동 자세 분류 및 평가 시연.
- 자세의 정확도 평가 기준:
  - **Perfect**: 모든 자세 정확
  - **Good**: 3개 이상 자세 정확
  - **Bad**: 정확한 자세가 2개 이하
- **한계점**:
  - 대용량 데이터로 인해 서버와 메모리 자원의 부족.
  - 데이터 분석 및 학습 시간 부족.

---

## 🛠️ 사용된 기술 스택

### **Programming Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### **Libraries and Frameworks**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)  
![Mediapipe](https://img.shields.io/badge/Mediapipe-009688?style=for-the-badge&logo=mediapipe&logoColor=white)

### **Visualization Tools**
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)

---

## 📊 주요 성과
- **운동 자세 분류 정확도**:
  - TSM 모델 기반으로 높은 정확도 달성.
- **실제 적용 가능성**:
  - 사용자 맞춤형 피드백 시스템으로 확장 가능.

---
- **활용 영상**:


https://github.com/user-attachments/assets/54e77049-d747-4d75-ad27-f6e016f77613



