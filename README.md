# ML in Production Tutorial 

In this repository I explore tips and tricks to deploy machine learning models with Docker following [http://mlinproduction.com/](http://mlinproduction.com/) posts. 

## Setup 

1. Create virtual environment: 
```bash
make env
```

2. Activate environment and install python packages:
```bash
make install
```

## Generate Data 

```bash
make generate_data
```

## Train Model

```bash
make train
```

## Generate Predictions

```bash
make inference
```
---

## Build Docker image
```bash
docker build -t docker-model .
```

## Generate Predictions

```bash
docker run docker-model python3 inference.py
```

## API

Run docker container:
```bash
docker run -it -p 5000:5000 docker-model python3 api.py
```
Request predictions (example):
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"x": 1.2}' 127.0.0.1:5000/predict
```
