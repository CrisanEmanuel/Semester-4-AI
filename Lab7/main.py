from sepiaTone import *
from data import *
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten

if __name__ == '__main__':
    # apply_sepia_to_folder('input_folder', 'output_folder')
    # Load the data
    inputs, outputs = load_images_from_folder('images/all')

    # Conversia la numpy array
    inputs = np.array(inputs)
    outputs = np.array(outputs)

    # Împărțirea datelor în set de antrenare și set de test
    train_images, test_images, train_labels, test_labels = train_test_split(inputs, outputs, test_size=0.2,
                                                                            random_state=42)
    # Definirea arhitecturii modelului
    # Definirea modelului ANN
    model = Sequential([
        Flatten(input_shape=(100, 100, 3)),  # Aplanăm imaginea într-un vector unidimensional
        Dense(128, activation='relu'),  # Strat dens cu 128 de neuroni și funcție de activare ReLU
        Dense(1, activation='sigmoid')  # Stratul de ieșire cu o singură unitate și funcție de activare sigmoid
    ])

    # Compilarea modelului
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Antrenarea modelului
    model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(test_images, test_labels))

    # Evaluarea modelului pe setul de test
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test accuracy:', test_acc)

