import scipy.ndimage, scipy.misc, numpy
import skvideo.io
import json
import matplotlib.pyplot as plt
import cv2
import os

def get_frame(time, frame_rate):
	t = time.split(':')
	s = int(t[1]) + 60 * int(t[0])
	return frame_rate * s

videoname = 'aslAlphabet.mp4'
afile = 'annotations.txt'
foldername = 'dataset5/annotations'
allletters = 'abcdefghiklmnopqrstuvwxy'

if not os.path.exists(foldername):
	os.mkdir(foldername)
	for a in allletters:
		os.mkdir(os.path.join(foldername, a))

annotations = open(afile, 'r').read().split('\n')[:-1]
#vc = cv2.VideoCapture(videoname)
#vc = skvideo.io.VideoCapture(videoname)
vc = skvideo.io.vreader(videoname)
metadata = skvideo.io.ffprobe(videoname)

#print(json.dumps(metadata['video'], indent=4))

frame_rate = metadata['video']['@r_frame_rate']
print(frame_rate)
num, denom = frame_rate.split('/')
frame_rate = round(float(num) / float(denom)) #in frames per second

letters, starts, ends = [], [], []

#need to convert times to frame rates
for line in annotations:
	toks = line.split()
	letters.append(toks[0])
	starts.append(get_frame(toks[1], frame_rate))
	ends.append(get_frame(toks[2], frame_rate))

print(letters)
print(starts)
print(ends)

count = -1
lettercount = 0
ind = 0
prevletter = 'J'

#cv2.namedWindow('preview')

for frame in vc:
	#cv2.imshow('preview', frame)
	#key = cv2.waitKey(10)
	#if key == 27:
	#		break
	count = count + 1
	if ind >= len(starts):
		continue

	if count < starts[ind]:
		continue
	if count > ends[ind]:
		ind = ind + 1
		lettercount = 0
		continue
	letter = letters[ind]
	resized = scipy.misc.imresize(frame, (150, 150, 3))
	#print(os.path.join(foldername, letter + '_' + str(lettercount) + '.png'))
	folder = os.path.join(foldername, letter.lower())
	#print(folder)
	fname = os.path.join(folder, letter + '_' + str(lettercount) + '.png')
	#	print(fname)
	cv2.imwrite(fname, resized)
	lettercount = lettercount + 1
	#if letter == prevletter:
	#	continue
	#prevletter = letter
	#print(letter)

cv2.destroyWindow('preview')
