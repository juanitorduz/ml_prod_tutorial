venv: 
	virtualenv venv

install:
	source venv/bin/activate;
	pip install -r requirements.txt

generate_data:
	python generate_data.py

train:
	mkdir model
	python train.py

inference:
	python inference.py
