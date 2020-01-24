import pytest
from generate_data import *
import pandas as pd

def test_generate_linear_data():
    generate_linear_data(n=100, betas=(1.0, 3.0), sigma=0.2)
    df = pd.read_csv('data/train_data.csv')
    assert df.shape == (100, 2)
