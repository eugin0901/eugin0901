import cv2

def display_image():

    img1 = cv2.imread('c:/users/user/workspace/example/night111.jpg', cv2.IMREAD_GRAYSCALE)
    #영상정보출력
    print("(rows,cols,ch):{}".format(img1.shape))

    #영상출력을 윈도우 생성
    cv2.namedWindow('img1',cv2.WINDOW_NORMAL)
    
    #윈도우에 영상 출력
    cv2.imshow('img1',img1)

    #사용자 입력 대기
    cv2.waitKey()
    #윈도우 파괴
    cv2.destroyAllWindows()



if __name__ == '__main__':
    #OpenCV 이용해서 영상 데이터 로딩
    image = cv2.imread('c:/users/user/workspace/example/night111.jpg',cv2.IMREAD_GRAYSCALE)
    if(image is None) :
        print('{}:reading error'.format(image))
    else:
        #윈도우에 영상 출력
        display_image()

# 이미지 출력
    display_image()