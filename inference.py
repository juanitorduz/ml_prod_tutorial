import os
from joblib import load
from utils import load_data


MODEL_DIR = os.environ['MODEL_DIR']
MODEL_FILE = os.environ['MODEL_FILE']
METADATA_FILE = os.environ['METADATA_FILE']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)


def predict(data_path):
    # Load data.
    X, y = load_data(data_path)
    # Load model
    print('Loading model from: {}'.format(MODEL_PATH))
    lin_model = load(MODEL_PATH)
    # Run inference
    print('Scoring observations...')
    y_pred = lin_model.predict(X)
    print(y_pred)
    return None


if __name__ == '__main__':
    predict('data/train_data.csv')