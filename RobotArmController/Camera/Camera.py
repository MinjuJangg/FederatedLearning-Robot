import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-x", type= int, required= False)

parser.add_argument("-y", type= int, required= False)

args = parser.parse_args()
class Camera():
    def __init__(self):
        self.capture = cv.VideoCapture(0)

        self.capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
        self.x = args.x
        self.y = args.y
        
    def imageCapture(self):
        self.ret, self.origin = self.capture.read()
        self.grey = cv.cvtColor(self.origin, cv.COLOR_BGR2GRAY)
        _, self.loc_bin = cv.threshold(self.grey, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        adp_bin = cv.adaptiveThreshold(self.grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 5)
        self.smooth = cv.GaussianBlur(self.grey, (95, 95), 0)
        self.gaussian = cv.divide(self.grey, self.smooth, scale = 192)
        _, self.loc_div_bin = cv.threshold(self.gaussian, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        self.adp_div_bin = cv.adaptiveThreshold(self.gaussian, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 5)
        
        cv.imwrite(f'./Data/rgb/{self.x}_{self.y}.jpg', self.origin)
        cv.imwrite(f'./Data/greyscale/{self.x}_{self.y}.jpg', self.grey)
        cv.imwrite(f'./Data/localized_bin/{self.x}_{self.y}.jpg', self.loc_bin)
        cv.imwrite(f'./Data/adaptive_bin/{self.x}_{self.y}.jpg', adp_bin)
        cv.imwrite(f'./Data/gaussian_blur/{self.x}_{self.y}.jpg', self.gaussian)
        cv.imwrite(f'./Data/gaussian_localized_bin/{self.x}_{self.y}.jpg', self.loc_div_bin)
        cv.imwrite(f'./Data/gaussian_adaptive_bin/{self.x}_{self.y}.jpg', self.adp_div_bin)

        self.capture.release()

if __name__ == "__main__":
    camera = Camera()
    camera.imageCapture()