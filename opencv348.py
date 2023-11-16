import sys
import numpy as np
import cv2


src = cv2.imread('pepper.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
#src이미지를 BGR에서 YCrCb로 변환
#cvtColor는 두개인수를 받아 원본이미지와 색상변환한 이미지를 받습니다.

ycrcb_planes = list(cv2.split(src_ycrcb))
#split메소드는 ycrcb  색이미지를 색상평면으로 분리하는 것이다.
#휘도(Y), 색도 적(Cr), 색도 청(Cb)
#분리해서 3개의 배열리스트로 반환

ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])
#하나의 인수를 받아 인력한 이미지를 히스토그램평활화를 적용
#히스토그램을 조정하여 강도 값을 더 균일하게 분산한다.
#이미지의 대비를 향상시킨다.


dst_ycrcb = cv2.merge(ycrcb_planes)
#YCrCb 이미지로 병합한다.
#cv2.merge()함수는 NumPy 배열의 리스트를 입력받고 병합된 이미지를 나타내는 단일 NumPy배열을 반환

dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)
#dst변수는 dst_ycrcb를 받아 YCrCb색공간에서 BGR색공간으로 변환

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()