FROM python:3.14.7

WORKDIR /app

COPY *.py . 
COPY *.json . 

CMD ["python","app.py"]