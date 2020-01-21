import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from joblib import load
import numpy as np
from envs import envs

MODEL_DIR = envs['MODEL_DIR']
MODEL_FILE = envs['MODEL_FILE']
METADATA_FILE = envs['METADATA_FILE']
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

ml_mod = load(MODEL_PATH)

app = Flask(__name__)
api = Api(app)


class Prediction(Resource):
    def __init__(self):
        self._required_features = ['x']
        self.reqparse = reqparse.RequestParser()
        for feature in self._required_features:
            self.reqparse.add_argument(
                feature,
                type=float,
                required=True,
                location='json',
                help='No {} provided'.format(feature)
            )
        super(Prediction, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        X = np.array([args[f] for f in self._required_features]).reshape(-1, 1)
        y_pred = ml_mod.predict(X)
        return {'prediction': y_pred.tolist()[0]}


api.add_resource(Prediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
