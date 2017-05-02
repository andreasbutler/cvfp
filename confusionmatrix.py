import os
from keras.models import load_model
import numpy as np
import scipy.ndimage
import skimage.color
from keras.preprocessing.image import ImageDataGenerator

model = load_model('letter_classifier.h5')
model.summary()

validation_data_dir = os.path.join(os.path.join('CNN_input','depth_data'), os.path.join('test'))

test_datagen = ImageDataGenerator(rescale=1./255)

batch_size = 16
img_height, img_width = 256, 256

num_images_per_class = [0] * 24
subdirs = [x[0] for x in os.walk(validation_data_dir)]
count = 0
for sd in subdirs:
    if sd == validation_data_dir:
        continue
    files = os.listdir(sd)
    if 'Thumbs.db' in files:
        num_images_per_class[count] = len(files) - 1
    else:
        num_images_per_class[count] = len(files)
    count += 1

print(num_images_per_class)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse',
    shuffle=False
)

#print(validation_generator.filenames)
print(len(validation_generator.filenames))

predictions = model.predict_generator(
    generator=validation_generator,
    steps=300,
)

#indices = validation_generator.class_indices

print(predictions.shape)

curr_predict = 0
counter = 0
conf = np.zeros((24, 24))

for i in range(predictions.shape[0]):
    predict = np.argmax(predictions[i, :])
    #print(predict, curr_predict)
	
    conf[curr_predict, predict] += 1
    counter += 1
    if counter >= num_images_per_class[curr_predict]:
        counter = 0
        curr_predict += 1
    if curr_predict >= 24:
	    curr_predict = 0

for i in range(conf.shape[0]):
    total = np.sum(conf[i, :])
    if total == 0:
        total = 1
    conf[i, :] = np.divide(conf[i, :], total)

letters = 'abcdefghiklmnopqrstuvwxy'
outstr = 'let'
for i in letters:
    outstr +='\t' + i
print(outstr)
for x in range(conf.shape[0]):
    out = letters[x] + '\t'
    for y in range(conf.shape[1]):
        out += '%1.4f\t' % conf[x, y]
    print(out)