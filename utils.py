import pandas as pd


def load_data(data_path):
    """Reads model data. It must have columns named 'x' and 'y'.
    :param data_path: path to the data.
    :return: Tuple of length two. Design matrix and target vector.
    """
    df = pd.read_csv(data_path)
    X = df['x'].values.reshape(-1, 1)
    y = df['y'].values.reshape(-1, 1)
    return X, y
