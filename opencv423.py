import sys
import numpy as np
import cv2
import random

#vtest.avi 영상을 cap 변수에 저장하여 비디오 파일을 엽니다.
cap = cv2.VideoCapture('vtest.avi')

#오픈이 안될때는 오류코드를 출력합니다.
if not cap.isOpened():
    print('Video open failed!')
    sys.exit()


#HOG디스크립터 객체 생성 및 기본 사람 검출기 설정을 합니다. 
hog = cv2.HOGDescriptor()
#HOG 디스크립터 객체를 생성합니다. HOG 디스크립터는 이미지에서 특징을 추출하는 데 사용되는 기술입니다.
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#HOG 디스크립터 객체를 기본 사람 검출기로 설정합니다. 기본 사람 검출기는 이미지에서 사람을 감지하는 데 사용되는 사전 학습된 분류기입니다.


#비디오 프레임 바복
while True:
    ret, frame = cap.read()

    if not ret:
        break

		#비디오 프레임에서 사람감지
    detected, _ = hog.detectMultiScale(frame)

		#감지된 사람마다 사각형 그리기
    for (x, y, w, h) in detected:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y), (x + w, y + h), c, 3)
				#src사각형을 그릴 이미지 / (x, y) 사각형의 왼쪽 상단 모서리 좌표/ (x + w, y + h) 사각형의 오른쪽 하단 모서리 좌표 / (r, g, b) 사각형의 색상 /thickness: 사각형의 두께
		
		#프레임 표시
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
		#10밀리초 동안 키보드 입력을 대기합니다. Esc 키가 입력되면 루프를 종료합니다.
        break

#모든창 닫기
cv2.destroyAllWindows()