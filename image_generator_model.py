import tensorflow as tf
from tensorflow import keras
import matplotlib.pylab as plt









fashion_mnist = keras.datasets.fashion_mnist
(image_train_full,label_train_full),(image_test,label_test) = fashion_mnist.load_data()
image_valid, image_train = image_train_full[:5000]/255.0 , image_train_full[5000:]/255.0
label_valid, label_train = label_train_full[:5000] , label_train_full[5000:]



encoder = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(100, activation="selu"),
    keras.layers.Dense(30, activation="selu"),
])
decoder = keras.models.Sequential([
    keras.layers.Dense(100, activation="selu", input_shape=[30]),
    keras.layers.Dense(28 * 28, activation="sigmoid"),
    keras.layers.Reshape([28, 28])
])
model_autoencoder = keras.models.Sequential([encoder, decoder])
model_autoencoder.compile(loss="binary_crossentropy",optimizer=keras.optimizers.SGD(learning_rate=1.5))

history = model_autoencoder.fit(image_train, image_train, epochs=10,validation_data=[image_valid, image_valid])

decoder.compile(optimizer=keras.optimizers.SGD(learning_rate=1.5), loss="binary_crossentropy")



model_autoencoder.save("autoencoder.h5")
encoder.save("encoder.h5")
decoder.save("decoder.h5")










