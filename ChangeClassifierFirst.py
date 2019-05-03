import numpy as np
import cv2

class ChangeClassifier:

    def __init__(self, pathToImage):
        self.img = cv2.imread(pathToImage)

    def detect_circles(self):
        modified_img = self.img.copy()
        gray_scale_img = cv2.cvtColor(modified_img, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray_scale_img, cv2.HOUGH_GRADIENT, 1.2, 300)
        print(circles)
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            template = np.copy(gray_scale_img[x-r:x+r, y-r:y+r])  # right eye
            cv2.imshow("output", template)
            cv2.waitKey(0)
            cv2.circle(modified_img, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(modified_img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        cv2.imshow("output", template)
        cv2.waitKey(0)

    # def type_of_coin(self, coin_image):

tester = ChangeClassifier("testimg4.jpg")
tester.detect_circles()