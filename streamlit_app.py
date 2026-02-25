import streamlit as st

st.set_page_config(page_title="Мой дашборд", layout="wide")
st.title("📊 Аналитика из Superset")

# Встраиваем дашборд — ИСПРАВЛЕНО
st.components.v1.iframe(
    src="https://misty-river-917.gopublic.su/superset/dashboard/12/?standalone=1",
    width=1200,
    height=800,
    scrolling=True
)
