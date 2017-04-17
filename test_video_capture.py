'''
Goal of this is to figure out how to pull frames from video input (ideally webcam input)
'''

import cv2
from keras.models import load_model
import scipy.ndimage, scipy.misc, numpy

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

#Get first frame
if vc.isOpened():
	rval, frame = vc.read()
else:
	rval = False

currletter = -1

model = load_model('letter_classifier.h5')

#model.summary()

letters = 'abcdefghiklmnopqrstuvwxy'

while rval:
	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	resized = scipy.misc.imresize(frame, (150, 150, 3))
	resized = numpy.expand_dims(resized, axis=0)
	vec = model.predict(resized)
	val = numpy.argmax(vec)
	#print(letters[val], val, vec)
	if val != currletter:
		print(letters[val])
		currletter = val
	key = cv2.waitKey(20)
	#Break if escape is pressed
	if key == 27:
		break

cv2.destroyWindow("preview")
