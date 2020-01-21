import json
import os
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from envs import envs
from utils import load_data

MODEL_DIR = envs['MODEL_DIR']
MODEL_FILE = envs['MODEL_FILE']
METADATA_FILE = envs['METADATA_FILE']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)


def generate_model_metadata(X, y, model):
    """Get model metadata:
        - mse
        - r2 score
    :param X: Design matrix.
    :param y: Target variable.
    :param model: Model for which we generate metadata.
    :return: Dictionary storing the metadata.
    """
    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    metadata = {
        'mean_square_error': mse,
        'r2 score': r2,
    }

    return metadata


def train(data_path):
    """Train simple linear regression with two variables y ~ x.
    Serialize model and metadata.
    :param data_path: path of the training data as csv.
    :return: None
    """
    X_train, y_train = load_data(data_path)

    ml_model = LinearRegression()
    ml_model.fit(X_train, y_train)

    metadata = generate_model_metadata(X_train, y_train, ml_model)

    # Serialize model and metadata.
    print('Serializing model to: {}'.format(MODEL_PATH))
    dump(ml_model, MODEL_PATH)

    print('Serializing metadata to: {}'.format(METADATA_PATH))
    with open(METADATA_PATH, 'w') as outfile:
        json.dump(metadata, outfile)

    return None


if __name__ == '__main__':
    train(data_path='data/train_data.csv')
