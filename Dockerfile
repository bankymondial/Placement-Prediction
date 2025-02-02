FROM python:3.12.1-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "predict-test.py", "model.bin", "./"]

EXPOSE 9090

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9090", "predict:app"]