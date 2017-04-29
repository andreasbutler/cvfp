import cv2
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
while True:
    img1 = 0
    img2 = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            #img_name = "opencv_frame_{}.png".format(img_counter)
            #cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            #img_counter += 1
            img1 = frame
            break
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            #img_name = "opencv_frame_{}.png".format(img_counter)
            #cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            #img_counter += 1
            img2 = frame
            break
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img1 = cv2.convertScaleAbs(img1)
    img2 = cv2.convertScaleAbs(img2)

    # print(img1.dtype)
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(img2,img1)
    cv2.imshow("img1",img2)
    cv2.imshow("img2",img1)
    plt.imshow(disparity,'gray')
    plt.show()
cam.release()

cv2.destroyAllWindows()