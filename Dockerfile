FROM python:3.11

WORKDIR /app

COPY receive_graph.py /app/receive_graph.py
RUN pip install -r requirements.txt

CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "8001"]
