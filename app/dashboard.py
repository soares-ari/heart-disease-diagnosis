import streamlit as st
import requests

st.set_page_config(page_title="Diagnóstico Cardíaco", page_icon="🫀")

# Inicializa etapa
if "etapa" not in st.session_state:
    st.session_state.etapa = 1

# Breadcrumb
st.markdown(f"### Etapa {st.session_state.etapa} de 3")

# Etapa 1: Dados básicos
if st.session_state.etapa == 1:
    st.header("🧍 Dados do paciente")
    st.session_state.idade = st.number_input("Idade", min_value=1, max_value=120, value=50)
    st.session_state.sexo = st.selectbox("Sexo", options=[("Masculino", 1), ("Feminino", 0)])
    st.session_state.cp = st.selectbox("Tipo de dor no peito", options=[(0, "Tipo 0"), (1, "Tipo 1"), (2, "Tipo 2"), (3, "Tipo 3")])
    if st.button("Próximo"):
        st.session_state.etapa = 2

# Etapa 2: Exames clínicos
elif st.session_state.etapa == 2:
    st.header("🧪 Exames clínicos")
    st.session_state.trestbps = st.number_input("Pressão arterial em repouso", value=130)
    st.session_state.chol = st.number_input("Colesterol sérico", value=250)
    st.session_state.fbs = st.selectbox("Glicose em jejum > 120 mg/dl", options=[("Não", 0), ("Sim", 1)])
    st.session_state.restecg = st.selectbox("Resultado do ECG", options=[0, 1, 2])
    st.session_state.thalach = st.number_input("Frequência cardíaca máxima", value=150)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Voltar"):
            st.session_state.etapa = 1
    with col2:
        if st.button("Próximo"):
            st.session_state.etapa = 3

# Etapa 3: Indicadores de esforço
elif st.session_state.etapa == 3:
    st.header("🏃 Indicadores de esforço")
    st.session_state.exang = st.selectbox("Angina induzida por exercício", options=[("Não", 0), ("Sim", 1)])
    st.session_state.oldpeak = st.number_input("Depressão do ST", value=1.0, format="%.1f")
    st.session_state.slope = st.selectbox("Inclinação do ST", options=[0, 1, 2])
    st.session_state.ca = st.selectbox("Nº de vasos principais coloridos", options=[0, 1, 2, 3, 4])
    st.session_state.thal = st.selectbox("Talassemia", options=[0, 1, 2, 3])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Voltar"):
            st.session_state.etapa = 2
    with col2:
        if st.button("Enviar"):
            dados = {
                "idade": st.session_state.idade,
                "sexo": st.session_state.sexo[1],
                "cp": st.session_state.cp[0],
                "trestbps": st.session_state.trestbps,
                "chol": st.session_state.chol,
                "fbs": st.session_state.fbs[1],
                "restecg": st.session_state.restecg,
                "thalach": st.session_state.thalach,
                "exang": st.session_state.exang[1],
                "oldpeak": st.session_state.oldpeak,
                "slope": st.session_state.slope,
                "ca": st.session_state.ca,
                "thal": st.session_state.thal
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
