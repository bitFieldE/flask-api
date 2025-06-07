FROM python:3.13.3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# コンテナ起動時のコマンド
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]