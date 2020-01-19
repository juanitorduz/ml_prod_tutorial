FROM python:3.7

# Install dependencies:
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN rm ./requirements.txt

RUN mkdir model
ENV MODEL_DIR=model
ENV MODEL_FILE=lin_mod.joblib
ENV METADATA_FILE=metadata.json

COPY generate_data.py ./generate_data.py
COPY utils.py ./utils.py
COPY train.py ./train.py
COPY data/train_data.csv ./data/train_data.csv
COPY inference.py ./inference.py

RUN python3 train.py

