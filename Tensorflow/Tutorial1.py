import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_lables) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover','Dress', 'Coat', 'Scandal','Shirt','Sneaker', 'Bag','Ankle boot']

train_images = train_images/255.0
test_images = test_images/255.0

print(train_images[6])

plt.imshow(train_images[6], cmap=plt.cm.binary)
plt.show()