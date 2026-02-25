import streamlit as st

st.set_page_config(page_title="Мой дашборд", layout="wide")
st.title("📊 Аналитика из Superset")

# Встраиваем дашборд
st.components.v1.iframe(
    src="http://host.docker.internal:8088/superset/dashboard/p/12/?standalone=1",
    width=1200,
    height=800,
    scrolling=True
)
