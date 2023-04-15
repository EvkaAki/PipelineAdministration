FROM python:3.7 AS backend-kubeflow-wheel

WORKDIR /src
COPY ./components/crud-web-apps/common/backend .

RUN python3 setup.py bdist_wheel

FROM python:3.7

WORKDIR /package
COPY --from=backend-kubeflow-wheel /src .
RUN pip3 install .

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "/app/main.py"]
