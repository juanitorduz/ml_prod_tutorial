import json
import os
from joblib import dump
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from utils import load_data

MODEL_DIR = os.environ['MODEL_DIR']
MODEL_FILE = os.environ['MODEL_FILE']
METADATA_FILE = os.environ['METADATA_FILE']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)


def train(data_path):
    """Train simple linear regression with two variables y ~ x.
    Serialize model and metadata
    :param data_path: path of the training data as csv.
    :return: None
    """
    X_train, y_train = load_data(data_path)

    lin_model = LinearRegression()
    lin_model.fit(X_train, y_train)

    train_mse = mean_squared_error(y_train, lin_model.predict(X_train))

    metadata = {
        'train_mean_square_error': train_mse,
    }

    # Serialize model and metadata.
    print('Serializing model to: {}'.format(MODEL_PATH))
    dump(lin_model, MODEL_PATH)

    print('Serializing metadata to: {}'.format(METADATA_PATH))
    with open(METADATA_PATH, 'w') as outfile:
        json.dump(metadata, outfile)

    return None


if __name__ == '__main__':
    train(data_path='data/train_data.csv')
