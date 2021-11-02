import numpy as np
import joblib
import gen.pb.microservice_pb2 as pb
from math import ceil

class SVM:
    def __init__(self):
        print('Loading pickles')
        self.__scaler = joblib.load('models/scaler.pkl')
        self.__model = joblib.load('models/model.pkl')
        print('Pickles were loaded')

    def __ceil_prob(self, prob) -> float:
        return ceil(prob * 100 * 10) / 10

    def __get_probabilty(self, values: np.array) -> float:
        des = self.__model.decision_function([values])
        return 1 / (1 + np.exp(-des[0]))

    def __standartize_row(self, values: np.array) -> np.array:
        return self.__scaler.transform(np.array([values]))[0]

    def get_mark(self, req: pb.Marks.GetRequest) -> float:
        values = np.array([
            req.areasSquarePer100k,
            req.areasAmountPer100k,
            req.sportsAmountPer100k,
            req.subwayDistance,
            req.pollutionPercentage
        ])
        values = self.__standartize_row(values)
        prob = self.__get_probabilty(values)
        return self.__ceil_prob(prob)
