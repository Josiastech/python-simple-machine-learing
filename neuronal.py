from numpy import exp, array, random, dot

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2* random.random((number_of_inputs_per_neuron, number_of_neurons)) -1

class NeuronalNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

        # La función Sigmoid, que describe una curva en forma de S
        def __sigmoid(self, x):
            return 1 / (1 + exp(-x))

        def __sigmoid_derivative(self, x):
            return x * (1 - x)

        def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
            for iteration in xrange(number_of_training_iterations):
                output_from_layer1, output_from_layer2 = self.think(training_set_inputs)