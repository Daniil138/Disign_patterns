FROM python:3.10.14 as build
WORKDIR /app
EXPOSE 5000

# Готовим окружение
RUN pip install --upgrade pip
RUN pip install -U Flask
RUN pip install -U flask-restplus

# Копируем исходный код
COPY Src /app/Src
COPY main.py /app/

# Что скопировалось?
RUN echo $(ls -1)

# Запускаем
CMD [ "python", "main.py" ]


