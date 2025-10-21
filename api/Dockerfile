# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro (melhora o cache)
COPY requirements.txt ./

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
