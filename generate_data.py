import pandas as pd
import numpy as np

np.random.seed(42)


def generate_linear_data(n, betas, sigma):
    """Generate pandas df with x and y variables related by a linear equation.
    Export data as csv.
    :param n: Number of observations.
    :param betas: beta parameters.
    :param sigma: standard deviation
    :return: None
    """
    x = np.linspace(start=0.0, stop=1.0, num=n)
    y = betas[0] + betas[1]*x + np.random.normal(loc=1, scale=sigma, size=n)
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv('data/train_data.csv', index=False)
    return None


if __name__ == "__main__":
    generate_linear_data(n=100, betas=(1.0, 3.0), sigma=0.2)
