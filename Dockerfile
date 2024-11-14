# Usando Python com Debian Slim, mais compatível e leve
FROM python:3.10-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os requisitos e instalando dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código do projeto
COPY . .

# Expondo a porta 8000
EXPOSE 8000

# Comando para rodar as migrações e iniciar o Gunicorn
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 --workers 3 app.wsgi:application --log-file -
