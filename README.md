---

# ❤️ Diagnóstico de Doença Cardíaca com Machine Learning

Este projeto implementa um pipeline completo de *Machine Learning* — da análise exploratória ao deploy em produção — para construir uma solução preditiva capaz de identificar a presença de doença cardíaca com base em variáveis clínicas.

---

## 🎯 Objetivo

Desenvolver um modelo supervisionado que receba dados clínicos e retorne a probabilidade de presença de doença cardíaca.
A solução está disponível via **API (FastAPI)** e **interface interativa (Streamlit)**, ambas hospedadas em um ambiente **containerizado (Docker)** e servidas por **Nginx com HTTPS** na **AWS EC2**.

---

## 🚑 Desafios: Recuperação e Estabilização do Ambiente

Após uma falha crítica no daemon Docker e conflito de versões entre *snap* e *apt*, o ambiente de produção foi completamente restaurado por meio de um **processo de Disaster Recovery estruturado**, incluindo:

* Diagnóstico e correção de *socket corruption* e processos zumbis;
* Reconfiguração e rebuild de containers com `docker-compose.prod.yml`;
* Correção do Nginx (`proxy_pass` interno ajustado para containers);
* Inserção de rota de *health check* na API (`/` → status operacional);
* Verificação e restauração completa do SSL (*Let’s Encrypt*);
* Testes de conectividade via `curl` e validação HTTPS via navegador.

🟢 **Resultado:** ambiente 100% operacional e estável em produção, com resposta positiva em todos os endpoints e SSL ativo.

---

## 📦 Dataset

* **Fonte:** [Heart Disease Dataset - Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
* **Variáveis:** idade, sexo, pressão arterial, colesterol, eletrocardiograma, frequência cardíaca, entre outras
* **Target:** presença (`1`) ou ausência (`0`) de doença cardíaca

---

## 🧪 Ciclo de Vida Aplicado

1. **Análise Exploratória** (`notebooks/01_eda.ipynb`)
2. **Modelagem e Avaliação** (`notebooks/02_modelagem.ipynb`)
3. **Treinamento e Exportação do Modelo** (`model/random_forest.pkl`)
4. **Deploy da API** com **FastAPI** (`api/main.py`)
5. **Interface Interativa** com **Streamlit** (`app/dashboard.py`)
6. **Containerização e Orquestração** com **Docker + Docker Compose**
7. **Serviço Web** com **Nginx** e **HTTPS automático (Let’s Encrypt)**
8. **Infraestrutura** em **AWS EC2 (Ubuntu 24.04 + Elastic IP)**
9. **Disaster Recovery** completo documentado e executado com sucesso ✅

---

## 🧠 Modelos Avaliados

* Regressão Logística
* Árvore de Decisão
* Random Forest ✅
* SVM
* KNN
* MLP

> O modelo **Random Forest** foi selecionado para deploy por apresentar o melhor equilíbrio entre acurácia, robustez e interpretabilidade.

---

## 🚀 Tecnologias Utilizadas

| Categoria           | Ferramentas                                      |
| ------------------- | ------------------------------------------------ |
| Linguagem           | Python 3.11                                      |
| Análise e Modelagem | Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn |
| API                 | FastAPI + Uvicorn                                |
| Frontend            | Streamlit                                        |
| Infraestrutura      | Docker, Docker Compose                           |
| Servidor Web        | Nginx (proxy reverso)                            |
| Certificados        | Let’s Encrypt (Certbot)                          |
| Cloud               | AWS EC2 (Ubuntu, Elastic IP)                     |
| Controle de Versão  | Git + GitHub                                     |
| Observabilidade     | Health check `/` + logs Nginx e containers       |

---

## 📁 Estrutura do Projeto

```
heart-disease-diagnosis/
│
├── api/
│   ├── main.py               # API FastAPI
│   ├── requirements.txt
│   └── Dockerfile
│
├── dashboard/
│   ├── dashboard.py          # Interface Streamlit
│   ├── requirements.txt
│   └── Dockerfile.streamlit
│
├── model/
│   └── random_forest.pkl     # Modelo treinado
│
├── notebooks/
│   ├── 01_eda.ipynb          # Análise exploratória
│   └── 02_modelagem.ipynb    # Treinamento e avaliação
│
├── docker-compose.yml        # Orquestração dos serviços
├── nginx/
│   └── heart-disease.conf    # Configuração unificada de proxy reverso
│
├── README.md
└── LICENSE
```

---

## 🧪 Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/heart-disease-diagnosis.git
cd heart-disease-diagnosis

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale dependências
pip install -r api/requirements.txt
pip install -r dashboard/requirements.txt

# Execute a API localmente
uvicorn api.main:app --host 0.0.0.0 --port 8000

# Execute a interface
streamlit run dashboard/dashboard.py
```

---

## 🐳 Execução com Docker

```bash
# Build e inicialização dos containers
docker compose up -d --build

# Verificar serviços ativos
docker ps

# API acessível em:
# http://localhost:8000/docs

# Dashboard acessível em:
# http://localhost:8501
```

---

## ☁️ Deploy em Produção (AWS EC2)

A aplicação completa roda em:

* **Ubuntu 24.04 (EC2 Instance)**
* **Nginx** como proxy reverso
* **HTTPS (Let’s Encrypt)**
* **Elastic IP fixo:** `3.132.89.3`
* **Domínios configurados via GoDaddy:**

  * [https://api.heartdiseaseapp.com](https://api.heartdiseaseapp.com)
  * [https://app.heartdiseaseapp.com](https://app.heartdiseaseapp.com)

---

## 🧱 Infraestrutura de Produção

A aplicação está hospedada em um ambiente **containerizado e seguro na AWS EC2**, utilizando **Nginx como proxy reverso** e **certificados HTTPS automáticos (Let’s Encrypt)**.
O fluxo de requisições segue a arquitetura abaixo:

![Arquitetura de Produção](./assets/infra-prod.png)

---

## 📈 Status do Projeto

| Etapa               | Status        |
| ------------------- | ------------- |
| EDA                 | ✅ Concluída   |
| Modelagem           | ✅ Concluída   |
| Avaliação           | ✅ Concluída   |
| Deploy API          | ✅ Online      |
| Interface Streamlit | ✅ Online      |
| Docker e AWS        | ✅ Em produção |
| Nginx + SSL         | ✅ Ativo       |
| Disaster Recovery   | ✅ Concluído   |

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.
Sinta-se à vontade para utilizar, modificar e redistribuir com os devidos créditos.

---

### 👨‍💻 Autor

**Ariel Soares**
Desenvolvedor e pesquisador em *Machine Learning*, com foco em aplicações práticas de IA, engenharia de sistemas e automação em nuvem.
📧 [LinkedIn](https://linkedin.com/in/ari-soares)

---
