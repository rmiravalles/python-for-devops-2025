FROM python:3.12-alpine3.21

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY alert-router.py .

EXPOSE 8000

CMD ["uvicorn", "alert-router.py", "--host", "0.0.0.0", "--port", "8000"]