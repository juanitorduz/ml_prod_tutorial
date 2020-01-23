FROM python:3.7

# Install dependencies:
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN rm ./requirements.txt

RUN mkdir model
ENV MODEL_DIR=model
ENV MODEL_FILE=lin_mod.joblib
ENV METADATA_FILE=metadata.json


ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION=eu-central-1

COPY envs.py ./envs.py
COPY generate_data.py ./generate_data.py
COPY utils.py ./utils.py
COPY train.py ./train.py
COPY inference.py ./inference.py
COPY api.py ./api.py

RUN python3 train.py

