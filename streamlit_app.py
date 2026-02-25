import streamlit as st

st.set_page_config(page_title="Мой дашборд", layout="wide")
st.title("📊 Аналитика из Superset")

# Ваши данные из скриншота
embed_id = "3f5f6297-0377-45c8-8cb9-be0d2ec269d2"
superset_domain = "https://cdca3dfa.us2a.app.preset.io"

# Формируем URL для встраивания
embed_url = f"{superset_domain}/embedded/{embed_id}?standalone=1"

# Встраиваем
st.components.v1.iframe(
    src=embed_url,
    width=1200,
    height=800,
    scrolling=True
)
