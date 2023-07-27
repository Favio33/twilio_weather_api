FROM python:3.10.12-slim-bullseye
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/main.py"]