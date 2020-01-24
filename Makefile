venv:
	virtualenv venv --python=python3.7

install:
	source venv/bin/activate;
	pip install -r requirements.txt

generate_data:
	mkdir -p data
	python generate_data.py

train:
	mkdir -p model
	python train.py

make docker_build:

	docker build -t docker-model \
		--build-arg AWS_REGION=$$(aws -- configure get region) \
		--build-arg AWS_ACCESS_KEY_ID=$$(aws configure get aws_access_key_id) \
		--build-arg AWS_SECRET_ACCESS_KEY=$$(aws -- configure get aws_secret_access_key) .
