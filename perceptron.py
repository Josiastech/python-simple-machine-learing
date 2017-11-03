import random

class perceptron:
    def __init__(self,input_number, step_size=0.1):
        self._ins = input_number #numero de parametros de entrada

        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size #La tasa de convergencia
     def predict(self, inputs):
         weighted_average = sum(w*elm for w, elm  in zip(self._w, inputs))