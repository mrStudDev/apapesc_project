# Usando Python com Debian Slim, mais compatível e leve
FROM python:3.10-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os requisitos e instalando dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice \
    unoconv \
    python3-uno \
    && rm -rf /var/lib/apt/lists/*
# Copiando o código do projeto
COPY . .

# Coletando os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expondo a porta 8000
EXPOSE 8000

# Comando para rodar as migrações e iniciar o Gunicorn
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 --workers 3 app.wsgi:application --log-file -
