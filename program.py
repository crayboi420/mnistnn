import numpy as np
import import_ipynb
import hashlib
# import neuralnetwork as nn

from keras.datasets import mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# layers = (784, 4, 10)
# x = np.ones((layers[0], 1))

# network = nn.model(layers)
# print(network.predict(x))
