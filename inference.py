import os
from joblib import load
from envs import envs
from utils import load_data


MODEL_DIR = envs['MODEL_DIR']
MODEL_FILE = envs['MODEL_FILE']
METADATA_FILE = envs['METADATA_FILE']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)


def predict(data_path):
    # Load data.
    X, y = load_data(data_path)
    # Load model
    print('Loading model from: {}'.format(MODEL_PATH))
    ml_model = load(MODEL_PATH)
    # Run inference
    print('Scoring observations...')
    y_pred = ml_model.predict(X)
    print(y_pred)
    return None


if __name__ == '__main__':
    predict('data/train_data.csv')
