import streamlit as st
import requests

st.markdown("## 🧾 Ficha Clínica do Paciente")
st.markdown("Preencha os dados abaixo para gerar o diagnóstico.")

with st.container():
    st.markdown("### 👤 Dados Pessoais")
    col1, col2 = st.columns(2)
    with col1:
        idade = st.number_input("Idade", min_value=1, max_value=120, value=50)
        sexo = st.selectbox("Sexo", options=[("Masculino", 1), ("Feminino", 0)])
    with col2:
        cp = st.selectbox("Tipo de dor no peito", options=[(0, "Tipo 0"), (1, "Tipo 1"), (2, "Tipo 2"), (3, "Tipo 3")])

st.divider()

with st.container():
    st.markdown("### 🧪 Exames Clínicos")
    col1, col2 = st.columns(2)
    with col1:
        trestbps = st.number_input("Pressão arterial em repouso", value=130)
        chol = st.number_input("Colesterol sérico", value=250)
        fbs = st.selectbox("Glicose em jejum > 120 mg/dl", options=[("Não", 0), ("Sim", 1)])
    with col2:
        restecg = st.selectbox("Resultado do ECG", options=[0, 1, 2])
        thalach = st.number_input("Frequência cardíaca máxima", value=150)

st.divider()

with st.container():
    st.markdown("### 🏃 Indicadores de Esforço")
    col1, col2 = st.columns(2)
    with col1:
        exang = st.selectbox("Angina induzida por exercício", options=[("Não", 0), ("Sim", 1)])
        oldpeak = st.number_input("Depressão do ST", value=1.0, format="%.1f")
    with col2:
        slope = st.selectbox("Inclinação do ST", options=[0, 1, 2])
        ca = st.selectbox("Nº de vasos principais coloridos", options=[0, 1, 2, 3, 4])
        thal = st.selectbox("Talassemia", options=[0, 1, 2, 3])

if st.button("📤 Enviar para Diagnóstico"):
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

