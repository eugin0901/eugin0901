import sys
import numpy as np
import cv2

#카메라열고,열기 여부를 확인합니다.
def main():
    cap = cv2.VideoCapture(0)
		
    if not cap.isOpened():
        print('비디오 열기 실패!')
        sys.exit()

    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()

        if not ret:
            print('프레임 로드 실패!')
            break

        # 창 크기에 맞게 프레임을 크기 조정합니다.
        frame = resize_frame(frame)

        # QR 코드를 감지하고 디코딩합니다.
        info, points, _ = detector.detectAndDecode(frame)

        if points is not None:
            # 감지된 QR 코드 주위에 다각형을 그립니다.
            points = np.array(points, dtype=np.int32).reshape(4, 2)
            cv2.polylines(frame, [points], True, (0, 0, 255), 2)

        if len(info) > 0:
            # 프레임에 QR 코드 정보를 오버레이합니다.
            cv2.putText(frame, info, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), lineType=cv2.LINE_AA)

        # 프레임을 표시합니다.
        cv2.imshow('frame', frame)

        # 캡처된 프레임을 해제합니다.
        del frame

        # 'Esc' 키를 누르면 종료합니다.
        if cv2.waitKey(1) == 27:
            break

    # 비디오 캡처 및 모든 창을 닫습니다.
    cap.release()
    cv2.destroyAllWindows()

#프레임의 크기를 창 크기에 맞춰 조정합니다.
def resize_frame(frame, max_width=640, max_height=480):
		#함수는 입력 이미지를 지정된 최대 너비와 높이에 맞게 크기 조정
    frame_height, frame_width, _ = frame.shape
    #프레임 치수 추출: 입력 이미지의 높이, 너비, 색상 채널을 추출합니다.

    if frame_height > max_height or frame_width > max_width:
        #크기 조정 확인: 프레임의 높이 또는 너비가 지정된 최대 치수를 초과하는지 확인합니다.               
        scale = min(max_height / frame_height, max_width / frame_width)
				#축소 비율 계산: 이미지를 최대 치수에 맞추기 위해 필요한 축소 비율을 결정합니다.
        resized_frame = cv2.resize(frame, dsize=None, fx=scale, fy=scale)
        #이미지 크기 조정: cv2.resize() 함수를 사용하여 계산된 축소 비율을 사용하여 입력 이미지를 크기 조정합니다.
    else:
        resized_frame = frame
				#크기 조정되지 않은 경우 처리: 프레임의 치수가 이미 지정된 최대 치수에 포함되어 있으면 원본 프레임을 단순히 반환합니다.
    return resized_frame
				#크기 조정된 프레임 반환: 크기 조정된 이미지를 반환합니다.

if __name__ == '__main__':
    main()