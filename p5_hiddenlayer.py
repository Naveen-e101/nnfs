import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X,y = spiral_data(100, 3)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, input):
        self.output = np.dot(input, self.weights) + self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0, input)


layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()

layer1.forward(X)
activation1.forward(layer1.output)

print(activation1.output)
