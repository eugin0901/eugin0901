import cv2

def display_image():
    #영상정보출력
    img1 = cv2.imread('c:/users/user/workspace/example/night111.jpg', cv2.IMREAD_COLOR)
    
    if img1 is None:
        print('image load failed!')
        return
      
    #영상정보출력
    print('type(img1):',type(img1))
    print('img1.shpe:', img1.shape)
    print("(rows,cols,ch):{}".format(img1.shape))

    if len(img1.shape) == 2 :
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3 :
        print('img1 is a truecolor image')

    #윈도우 생성
    cv2.namedWindow('img1',cv2.WINDOW_NORMAL)
    #윈도우에 영상 출력
    cv2.imshow('img1',img1)
    #사용자 입력 대기
    cv2.waitKey()
    #윈도우 파괴
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #OpenCV 이용해서 영상 데이터 로딩
    image = cv2.imread('c:/users/user/workspace/example/night111.jpg',cv2.IMREAD_COLOR)
    
# 이미지 출력
    display_image()