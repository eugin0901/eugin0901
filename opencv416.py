import numpy as np
import cv2

#kids.png 이미지를 로드합니다.
def detect_face():
    src = cv2.imread('kids.png')

#이미지가 성공적으로 로드되었는지 확인합니다. 아니면 오류메세지를 출력하고 반환합니다.
    if src is None:
        print('Image load failed!')
        return
		
		#얼굴 분류하는 메소드를 사용합니다. cv2.CascadeClassifier : 이미지에서 얼굴을 감지하는데 사용합니다.
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    #얼굴이 감지가 안되면 오류메세지를 출력하고 반환합니다.
    if classifier.empty():
        print('XML load failed!')
        return
		
		#classifier.detectMultiScale() 함수를 사용하여 이미지에서 얼굴을 감지합니다. 
		#이 함수는 감지된 얼굴을 나타내는 사각형 목록을 반환합니다.
    faces = classifier.detectMultiScale(src)
		
		#src에서 얼굴을 감지된 얼굴을 나타내는 사각형 목록을 반환한다. 
		#(x,y,w,h) 모서리좌표, (255,0,255) 사각형색상-파란색, (2) 사각형의 두께 
    for (x, y, w, h) in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 255), 2)
		
		#src이미지를 표시합니다.
    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()


def detect_eyes():
    src = cv2.imread('kids.png')

    if src is None:
        print('Image load failed!')
        return
		
		#cv2.CascadeClassifier()함수는 얼굴대신 눈을 감지하는 분류기를 생성한다.
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

    if face_classifier.empty() or eye_classifier.empty():
        print('XML load failed!')
        return

    faces = face_classifier.detectMultiScale(src)
		#src에서 얼굴을 감지, 이미지를 입력받아 감지된 얼굴을 나타내는 사각형 목록을 반환
		#왼족 모서리좌표 (x1,y1)/ 오른쪽하단 모서리좌표(x1+w1, y1+h1) / 사각형색상-파란색 (255,0255) / 사각형두께(2)
    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(src, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 255), 2)
        
				#감지된 얼굴 영역을 faceROI에 저장
        faceROI = src[y1:y1 + h1, x1:x1 + w1]
				#faceROI에서 눈을 감지하기, 감지된 눈을 나태나내는 사각형 목록을 반환한다.
        eyes = eye_classifier.detectMultiScale(faceROI)
				
        for (x2, y2, w2, h2) in eyes:
            #center변수에 눈의 중심좌표를 저장한다. 
						center = (int(x2 + w2 / 2), int(y2 + h2 / 2))
            #cv2.circle() 함수를 사용하여 감지된 눈 주위에 원을 그립니다.
						cv2.circle(faceROI, center, int(w2 / 2), (255, 0, 0), 2, cv2.LINE_AA)
						#눈의 중심 좌표 (x, y), 원의 반지름, 사각형의 색상 (255, 0, 0) (빨간색), 원의 두께 (2), 라인 스타일 (cv2.LINE_AA)을 입력

		#src이미지를 출력합니다.
    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_face()
    detect_eyes()