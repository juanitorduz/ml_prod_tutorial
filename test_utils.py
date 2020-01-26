import os
from envs import envs
from utils import load_data

S3_BUCKET = envs['S3BUCKET']
S3_DATA_PATH = os.path.join(
    's3://', S3_BUCKET, 'ml_prod_tutorial/data/train_data.csv'
)


def test_load_data_y_isvector():
    _, y = load_data(S3_DATA_PATH)
    assert y.shape[1] == 1


def test_load_data_X_ismatrix():
    X, _ = load_data(S3_DATA_PATH)
    assert X.shape[1] == 1


def test_load_data_X_y_same_dim():
    X, y = load_data(S3_DATA_PATH)
    assert X.shape[0] == y.shape[0]

