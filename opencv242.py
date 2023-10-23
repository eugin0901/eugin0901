import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.bitwise_and(src1, src2)
dst2 = cv2.bitwise_or(src1, src2)
dst3 = cv2.bitwise_xor(src1, src2)
dst4 = cv2.bitwise_not(src1)


cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('bitwise_and', dst1)
cv2.imshow('bitwise_or', dst2)
cv2.imshow('bitwise_xor', dst3)
cv2.imshow('bitwise_not', dst4)

cv2.waitKey()
cv2.destroyAllWindows()