FROM python:3.8-slim-buster

WORKDIR / .

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]