import streamlit as st

st.set_page_config(page_title="Мой дашборд", layout="wide")
st.title("📊 Аналитика из Superset")

# Ваши данные из скриншота
embed_id = "95c589d8-4a5b-420d-8d6b-96ed391c9c29"
superset_domain = "https://misty-river-917.gopublic.su"

# Формируем URL для встраивания
embed_url = f"{superset_domain}/embedded/{embed_id}?standalone=1"

# Встраиваем
st.components.v1.iframe(
    src=embed_url,
    width=1200,
    height=800,
    scrolling=True
)
