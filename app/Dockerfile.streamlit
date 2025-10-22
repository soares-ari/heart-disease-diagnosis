# Usa imagem base leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o restante do código do dashboard
COPY . .

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o app Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
