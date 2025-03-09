# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY ./requirements.txt /requirements.txt
COPY ./main.py /main.py
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Expone el puerto de la aplicación
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]
