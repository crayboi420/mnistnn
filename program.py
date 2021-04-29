import numpy as np
import matplotlib.pyplot as plt
# import neuralnetwork as nn

from tensorflow.keras.datasets import mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

print(training_images[4])
plt.imshow(training_images[4])

# layers = (784, 4, 10)
# x = np.ones((layers[0], 1))

# network = nn.model(layers)
# print(network.predict(x))
