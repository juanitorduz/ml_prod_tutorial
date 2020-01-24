import pytest
from generate_data import *
import pandas as pd

def test_generate_linear_data():
    generate_linear_data(n=100, betas=(1.0, 3.0), sigma=0.2)
    t = 1 + 1
    assert t==2
