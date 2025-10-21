# Diagnóstico de Doença Cardíaca com Machine Learning

Este projeto aplica o ciclo completo de Machine Learning — da análise exploratória ao deploy — para construir uma solução preditiva capaz de identificar a presença de doença cardíaca com base em variáveis clínicas.

---

## 🎯 Objetivo

Desenvolver um modelo supervisionado que receba dados clínicos e retorne a probabilidade de presença de doença cardíaca. A solução será disponibilizada via API e interface interativa.

---

## 📦 Dataset

- Fonte: [Heart Disease Dataset - Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- Variáveis: idade, sexo, pressão arterial, colesterol, eletrocardiograma, frequência cardíaca, entre outras
- Target: presença (`1`) ou ausência (`0`) de doença cardíaca

---

## 🧪 Ciclo de Vida Aplicado

1. **Análise Exploratória** (`01_eda.ipynb`)
2. **Modelagem e Avaliação** (`02_modelagem.ipynb`)
3. **Deploy via API (FastAPI)** (`api/main.py`)
4. **Interface interativa (Streamlit)** (`app/dashboard.py`)
5. **Containerização com Docker**

---

## 🧠 Modelos Testados

- Regressão Logística
- Árvore de Decisão
- Random Forest ✅
- SVM
- KNN
- MLP

> O modelo **Random Forest** foi selecionado para deploy por apresentar desempenho perfeito, alta robustez e interpretabilidade.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Pandas, Scikit-Learn, Matplotlib, Seaborn
- FastAPI
- Streamlit
- Docker
- Git + GitHub

---

## 📁 Estrutura do Projeto

heart-disease-diagnosis/ 
├── data/ 
├── notebooks/ 
│ ├── 01_eda.ipynb 
│ └── 02_modelagem.ipynb 
├── src/ 
├── api/ 
│ └── main.py 
├── app/ 
│ └── dashboard.py 
├── Dockerfile 
├── requirements.txt 
├── README.md


---

## 🧪 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/heart-disease-diagnosis.git
cd heart-disease-diagnosis

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale dependências
pip install -r requirements.txt

# Execute a API
uvicorn api.main:app --reload

# Execute a interface
streamlit run app/dashboard.py
```
---

📌 Status do Projeto
✅ EDA 
✅ Modelagem 
✅ Avaliação 
🔜 Deploy 
🔜 Interface 
🔜 Docker

---

📄 Licença
Este projeto está licenciado sob a MIT License.

---