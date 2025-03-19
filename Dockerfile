FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
