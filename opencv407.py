import sys
import numpy as np
import cv2

#이미지를 읽어옵니다.
img = cv2.imread('circuit.bmp', cv2.IMREAD_COLOR)
templ = cv2.imread('crystal.bmp', cv2.IMREAD_COLOR)

if img is None or templ is None:
    print('Image load failed!') #이미지를 로드하지 못하면 출력합니다.
    sys.exit()

#이미지의 밝기를 50씩 증가하여 조절을 합니다. 세 가지 값을 모두 50씩 증가시키기 위해 (50, 50, 50) 튜플을 사용하는 것
img = img + (50, 50, 50)


#노이즈 생성을 합니다. 
noise = np.zeros(img.shape, np.int32)
#cv2.randn() 함수는 정규분포에서 난수를 생성합니다.
#noise 배열에 평균이 0이고 표준편차가 10인 난수 생성
cv2.randn(noise, 0, 10)
# img와 noise 이미지를 더합니다.
img = cv2.add(img, noise, dtype=cv2.CV_8UC3)


#템플릿을 매칭해줍니다. #img, temp1의 미미지를 매칭함
res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
#이 결과값을 32비트 단일 채널 이미지로 반환합니다.


#매칭 결과를 정규화합니다.
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
#cv2.normalize()함수는 이미지의 밝기를 정규화합니다.


#최대 매칭 값을 찾습니다.
_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)
#cv2.minMaxLoc()함수는 이미지의 최소값, 최대값, 최소위치, 최대위치를 반환합니다.

#템플릿 크기를 추출합니다.
#temp1은 템플릿이미지의 높이와 너비를 가져옵니다.
(th, tw) = templ.shape[:2]

#매칭 위치에 사각형을 그립니다.(img 이미지에 maxloc 위치에 사각형을 그립니다.)
cv2.rectangle(img, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)


#이미지를 출력합니다.
cv2.imshow('templ', templ)
cv2.imshow('res_norm', res_norm)
cv2.imshow('img', img)
cv2.waitKey()
rurhcv2.destroyAllWindows()