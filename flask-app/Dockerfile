FROM python:3.8-slim-buster

WORKDIR / .

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "flask", "--app", "main", "run", "--host=0.0.0.0", "--debug"]