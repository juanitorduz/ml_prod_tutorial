import os
from joblib import load
from envs import envs
from utils import load_data


MODEL_DIR = envs['MODEL_DIR']
MODEL_FILE = envs['MODEL_FILE']
METADATA_FILE = envs['METADATA_FILE']
S3_BUCKET = envs['S3BUCKET']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)
S3_DATA_PATH = os.path.join(
    's3://', S3_BUCKET, 'ml_prod_tutorial/data/train_data.csv'
)


def predict(data_path):
    """ Generate predictions of the model for new data sored in `data_path`.
    Print the predictions as an output. 
    :param data_path: Path of the new data as csv.
    :return: None
    """
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
    predict(S3_DATA_PATH)
