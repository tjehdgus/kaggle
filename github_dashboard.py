import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 스토어 매출 예측 대시보드")

# GitHub에서 바로 불러오는 CSV 주소
url = "https://raw.githubusercontent.com/tjehdgus/kaggle/main/real4.csv"

try:
    df = pd.read_csv(url, encoding="cp949")
except:
    df = pd.read_csv(url, encoding="utf-8")

df["date"] = pd.to_datetime(df["date"])

store = st.selectbox("매장 번호 선택", sorted(df["store_nbr"].unique()))
family = st.selectbox("제품군 선택", sorted(df["family"].unique()))

filtered = df[(df["store_nbr"] == store) & (df["family"] == family)]

st.subheader(f"매장 {store} - 제품 '{family}' 예측 매출 추이")

fig = px.line(filtered, x="date", y="sales", markers=True,
              title="예측 매출 시계열 그래프",
              labels={"date": "날짜", "sales": "예측 매출"})

fig.update_traces(hovertemplate="날짜: %{x}<br>매출: %{y:.2f}")
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)



