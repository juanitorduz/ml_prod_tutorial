# ML in Production Tutorial 

In this repository I explore tips and tricks to deploy machine learning models with Docker + Kubernetes following [http://mlinproduction.com/](http://mlinproduction.com/) posts. 

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
