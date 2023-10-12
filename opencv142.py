import numpy as np
import cv2

def video_in():
    cap = cv2.VideoCapture('c:/Users/조유진/opencv_workspace/example/123.mp4')
    
    #videocapture 객체가 비디오를 성공적으로 열었는지 확인
    if not cap.isOpened():
        print("Video open failed!")
        return
    
    #성공적으로 열어준다. width(프레임너비), height(프레임높이), count(프레임수)를 가져온다.
    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    #프레임레이트를 나타낸다. 프레임레이트는 비디오에서 1초당 표시되는 프레임수를 말한다.
    fps = cap.get(cv2.CAP_PROP_FPS)
    #프레임레이트 출력
    print('FPS:', fps)
    #프레임을 표시하는데 필요한 지연시간을 계산한다.. round()는 소수점을 반올림하는 함수
    delay = round(1000 / fps)                    #1초당 표시되는 프레임수를 반올림함

    while True:                                     #무한루프
        ret, frame = cap.read()                     #비디오에서 프레임을 읽어온다. ret은 성공적으로 읽혔는지 여부를 나타내는 불리언값

        if not ret:                                 #프레임이 성공적으로 읽히지 않았다면 루프를 벗어난다.
            break                         

                             
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(delay) == 27:                #키보드에서 q를 눌렀는지 여부에 대해 확인, 반환하는 값이 27일떄 q가 눌러진다. 일반적으로 비디오 재생 및 루프 종료
            break

    cv2.destroyAllWindows()



#카메라에서 비디오를 녹화하는 것을 의미한다.
def camera_in_video_out():                 
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        return
    
    ##width(프레임너비), height(프레임높이), count(프레임수)을 정의한다.
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    #비디오 코덱을 지정하는 함수ㅡ 비디오 코덱은 비이오를 압축하고 압축해제하는데 사용되는 알고리즘이다.
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
    delay = round(1000 / fps)

    #비디오 출력함수, 비디오 프레임을 비디오 파일로 저장할 수 있다.
    outputVideo = cv2.VideoWriter(cap, fourcc, fps, (w, h))

    if not outputVideo.isOpened():
        print('File open failed!')
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

       
        outputVideo.write(inversed)

        cv2.imshow('frame', frame)
       
        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()


#파이썬 인터프리터가 이 코드 실행시 name 변수 값이 main으로 설정된다.
if __name__ == '__main__':
    video_in()                      #함수를 호출하여 카메라 또는 비디오 파일에서 비디오 프레임을 읽는다.
    camera_in_video_out()           #함수를 호출하여 비디오 프레임을 비디오 파일로 저장한다.
