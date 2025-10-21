import streamlit as st
import requests

st.set_page_config(page_title="Diagnóstico Cardíaco", page_icon="🫀")

st.title("⚕️ Diagnóstico de Doença Cardíaca")
st.markdown("Preencha os dados do paciente para obter o resultado.")

# Campos do formulário
with st.form("formulario"):
    idade = st.number_input("Idade", min_value=1, max_value=120, value=50)
    sexo = st.selectbox("Sexo", options=[("Masculino", 1), ("Feminino", 0)])
    cp = st.selectbox("Tipo de dor no peito", options=[(0, "Tipo 0"), (1, "Tipo 1"), (2, "Tipo 2"), (3, "Tipo 3")])
    trestbps = st.number_input("Pressão arterial em repouso", value=130)
    chol = st.number_input("Colesterol sérico", value=250)
    fbs = st.selectbox("Glicose em jejum > 120 mg/dl", options=[("Não", 0), ("Sim", 1)])
    restecg = st.selectbox("Resultado do ECG", options=[0, 1, 2])
    thalach = st.number_input("Frequência cardíaca máxima", value=150)
    exang = st.selectbox("Angina induzida por exercício", options=[("Não", 0), ("Sim", 1)])
    oldpeak = st.number_input("Depressão do ST", value=1.0, format="%.1f")
    slope = st.selectbox("Inclinação do ST", options=[0, 1, 2])
    ca = st.selectbox("Nº de vasos principais coloridos", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Talassemia", options=[0, 1, 2, 3])

    submitted = st.form_submit_button("Enviar")

# Envia para a API
if submitted:
    dados = {
        "idade": idade,
        "sexo": sexo[1],
        "cp": cp[0],
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs[1],
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang[1],
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    try:
        resposta = requests.post("http://127.0.0.1:8000/predict", json=dados)
        resultado = resposta.json()

        if resultado["doenca_cardiaca"]:
            st.error(f"⚠️ Risco detectado! Probabilidade: {resultado['probabilidade']*100:.1f}%")
        else:
            st.success(f"✅ Sem indícios de doença cardíaca. Probabilidade: {resultado['probabilidade']*100:.1f}%")

    except Exception as e:
        st.exception(f"Erro ao conectar com a API: {e}")
