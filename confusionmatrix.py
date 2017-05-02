import os
from keras.models import load_model
import numpy as np
import scipy.ndimage
import skimage.color

if __name__ == '__main__':
    model = load_model('letter_classifier.h5')
    model.summary()

    conf = np.zeros((24, 24)) #Output confusion matrix

    path="CNN_input\\depth_data\\test"
    subdirs = [x[0] for x in os.walk(path)]
    classification = -1
    for sd in subdirs:
        print(sd)
        if sd == path:
            continue
        classification += 1
        files = os.listdir(sd)
        for f in files:
            if f == 'Thumbs.db':
                continue
            filename = os.path.join(sd, f)
            img = scipy.ndimage.imread(filename)
            color = skimage.color.gray2rgb(img)
            img = np.expand_dims(color, axis=0)
            pred = model.predict(img)
            val = np.argmax(pred)
            #print(val)
            conf[classification, val] += 1

    for i in range(conf.shape[0]):
        conf[i, :] = np.divide(conf[i, :], np.sum(conf[i, :]))

    print(conf)

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