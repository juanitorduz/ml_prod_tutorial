
venv: 
	virtualenv venv

install:
	source venv/bin/activate; \
	pip install -r requirements.txt; \

generate_data:
	python generate_data.py

train:
	mkdir model
	export MODEL_DIR=model; \
	export MODEL_FILE=lin_mod.joblib; \
	export METADATA_FILE=metadata.json; \
	python train.py