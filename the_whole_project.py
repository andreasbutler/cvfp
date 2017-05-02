'''Trains a simple convnet on the MNIST dataset.
Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
import os

batch_size = 16
#num_classes = 31#23#24
num_classes=24
epochs = 12

nb_train_samples = 1500
nb_validation_samples = 300

# input image dimensions
img_height, img_width = 256, 256

# the data, shuffled and split between train and test sets
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

#Windows
# train_data_dir = os.path.join("dataset5","A")
# validation_data_dir = os.path.join("dataset5","A_validate")
train_data_dir = os.path.join(os.path.join("CNN_input","depth_data"), os.path.join("train"))
validation_data_dir = os.path.join(os.path.join("CNN_input","depth_data"), os.path.join("test"))

input_shape = (img_height, img_width, 3)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
#
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Dropout(0.25))
model.add(Flatten())
#model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.sparse_categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    #rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

#test_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse',
    color_mode='grayscale'
)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse',
    color_mode='grayscale'
)

model.fit_generator(
    generator = train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=epochs,				            # For Keras 2.0 API change to epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples//batch_size)

model.save('letter_classifier.h5')

