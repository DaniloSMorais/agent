# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que o Gunicorn vai usar
EXPOSE 80

# Comando para rodar a aplicação com Gunicorn
# 'app' é o nome do seu módulo Python, 'app' é a instância do Flask
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]