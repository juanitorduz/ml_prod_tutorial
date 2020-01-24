import pytest
from generate_data import *
import pandas as pd


def test_generate_linear_data_shape():
    generate_linear_data(n=100, betas=(1.0, 3.0), sigma=0.2)
    df = pd.read_csv('data/train_data.csv')
    assert df.shape == (100, 2)


def test_generate_linear_colnames():
    generate_linear_data(n=100, betas=(1.0, 3.0), sigma=0.2)
    df = pd.read_csv('data/train_data.csv')
    same_cols = df.columns == ['x', 'y']
    assert same_cols.all()
