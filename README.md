# ML in Production Tutorial 

In this repository I explore tips and tricks to deploy machine learning models with Docker + Kubernetes following [http://mlinproduction.com/](http://mlinproduction.com/) posts. 

## Setup 

1. Create virtual environment: 
```bash
virtualenv venv 
```

2. Activate environment:
```bash
source venv/bin/activate
```
3. Install requirements:
```bash
pip install -r requirements.txt
```

## Set ENV Variables

```bash
mkdir model
export MODEL_DIR=model
export MODEL_FILE=lin_mod.joblib
export METADATA_FILE=metadata.json
```

## Generate Data 

```bash
python generate_data.py
```