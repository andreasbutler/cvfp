from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

import cv2
import ctypes
import _ctypes
import pygame
import sys
import numpy as np

#from keras.models import load_model
import scipy.ndimage, scipy.misc
import skimage.color


cv2.namedWindow("preview")

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

# colors for drawing different bodies
SKELETON_COLORS = [pygame.color.THECOLORS["red"],
                    pygame.color.THECOLORS["blue"],
                    pygame.color.THECOLORS["green"],
                    pygame.color.THECOLORS["orange"],
                    pygame.color.THECOLORS["purple"],
                    pygame.color.THECOLORS["yellow"],
                    pygame.color.THECOLORS["violet"]]

#model = load_model('letter_classifier.h5')
#letters = 'abcdefghiklmnopqrstuvwxy0123456789'
#model.summary()

#print(len(letters))
currletter = -1

class InfraRedRuntime(object):
    def __init__(self):
        pygame.init()

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Loop until the user clicks the close button.
        self._done = False

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Kinect runtime object, we want only color and body frames
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

        # back buffer surface for getting Kinect infrared frames, 8bit grey, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.depth_frame_desc.Width, self._kinect.depth_frame_desc.Height), 0, 24)
        # here we will store skeleton data
        self._bodies = None

        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._kinect.depth_frame_desc.Width, self._kinect.depth_frame_desc.Height),
                                                pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

        pygame.display.set_caption("Kinect for Windows v2 Depth")



    def draw_depth_frame(self, frame, target_surface):
        if frame is None:  # some usb hub do not provide the infrared image. it works with Kinect studio though
            return
        frame2 = np.array(frame)
        frame2 = frame2.reshape((self._kinect.depth_frame_desc.Height, self._kinect.depth_frame_desc.Width))
        frame2[frame2 == 0] = np.amax(frame2) #Ignore points where depth sensor screwed up
        frame2[frame2 > 1.5 * np.amin(frame2)] = np.amax(frame2)
        frame2 = frame2/(np.amax(frame2))
        frame2[frame2 == 1] = 0
        print(np.amax(frame2), np.amin(frame2))
        #print(frame2.shape)
        #print(frame2)
        target_surface.lock()
        f8=np.uint8(frame.clip(1,4000)/16.)
        frame8bit=np.dstack((f8,f8,f8))

        #Try taking the central 256x256 pixels instead of resizing
        halfw, halfh = 128, 128
        xb1, xb2 = frame2.shape[0] / 2 - halfw, frame2.shape[0] / 2 + halfw
        yb1, yb2 = frame2.shape[1] / 2 - halfh, frame2.shape[1] / 2 + halfh

        center = frame2[xb1:xb2, yb1:yb2]

        colorframe = skimage.color.gray2rgb(center)
        resized = scipy.misc.imresize(colorframe, (256, 256, 3))

        cv2.imshow("preview", resized)

        #resized = np.expand_dims(resized, axis=0)
        '''
        vec = model.predict(resized)
        val = np.argmax(vec)
        global currletter
        if val != currletter:
            print(letters[val], val, vec)
            currletter = val
'''


        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame8bit.ctypes.data, frame8bit.size)
        del address
        target_surface.unlock()

    def run(self):
        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'],
                                                pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)


            # --- Getting frames and drawing
            if self._kinect.has_new_depth_frame():
                frame = self._kinect.get_last_depth_frame()
                self.draw_depth_frame(frame, self._frame_surface)
                frame = None

            self._screen.blit(self._frame_surface, (0,0))
            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        pygame.quit()


__main__ = "Kinect v2 InfraRed"
game =InfraRedRuntime();
game.run();