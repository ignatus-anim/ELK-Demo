FROM python:3.11-slim
WORKDIR /app
COPY app/ ./app/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p /app/logs
CMD ["python", "app/app.py"]
