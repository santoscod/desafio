# vai usar imagem do python
FROM python:3.11-slim

# as variaveis vao ser definidas
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dentro do conteiner
WORKDIR /app

# copias das dependencias
COPY requirements.txt /app/

# instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# copia todo o codigo do projeto para dentro do conteiner
COPY . /app/

# expõe a porta 8000
EXPOSE 8000

# comando para executar quando o conteiner iniciar
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]