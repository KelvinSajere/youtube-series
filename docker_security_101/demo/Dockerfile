FROM python:3.12

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
# Run as root (needed for demo / risky container)
USER root

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
