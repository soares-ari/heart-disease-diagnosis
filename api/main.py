from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Inicializa a API
app = FastAPI(title="Diagnóstico de Doença Cardíaca")

# Carrega o modelo treinado
modelo = joblib.load("model/random_forest.pkl")

# Define os campos esperados na requisição
class DadosPaciente(BaseModel):
    idade: float
    sexo: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Rota principal
@app.post("/predict")
def prever_doenca(dados: DadosPaciente):
    entrada = np.array([[dados.idade, dados.sexo, dados.cp, dados.trestbps, dados.chol, dados.fbs,
                     dados.restecg, dados.thalach, dados.exang, dados.oldpeak,
                     dados.slope, dados.ca, dados.thal]])
    
    predicao = modelo.predict(entrada)[0]
    probabilidade = modelo.predict_proba(entrada)[0][1]

    return {
        "doenca_cardiaca": bool(predicao),
        "probabilidade": round(probabilidade, 4)
    }
