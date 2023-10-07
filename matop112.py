import cv2
import numpy as np

def mat_op1():
    img1 = np.empty((0, 0), dtype=np.uint8)  # empty matrix
    img2 = np.zeros((480, 640), dtype=np.uint8)  # unsigned char, 1-channel
    img3 = np.zeros((480, 640, 3), dtype=np.uint8)  # unsigned char, 3-channels
    img4 = np.zeros((480, 640, 3), dtype=np.uint8)  # Size(width, height)

    img5 = np.full((480, 640), 128, dtype=np.uint8)  # initial values, 128
   
    mat1 = np.zeros((3, 3), dtype=np.int32)  # 0's matrix
    mat2 = np.ones((3, 3), dtype=np.float32)  # 1's matrix
    mat3 = np.eye(3, dtype=np.float32)  # identity matrix

    data = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32)
    mat4 = np.reshape(data, (2, 3))

    mat5 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
   
    mat4 = np.zeros((256, 256, 3), dtype=np.uint8)  # uchar, 3-channels
    mat5 = np.zeros((4, 4), dtype=np.float32)  # float, 1-channel

    mat4[:, :] = (255, 0, 0)
    mat5[:, :] = 1.0

    
def mat_op2():
    img1 = cv2.imread("dog.bmp")

    img2 = img1.copy()
    img3 = np.copy(img1)

    img4 = img1.copy()
    img5 = np.copy(img1)

    img1[:, :] = (0, 255, 255)  # yellow
    img2[:, :] = (0, 255, 255)
    img3[:, :] = (0, 255, 255)
    
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
    cv2.imshow("img4", img4)
    cv2.imshow("img5", img5)

    cv2.waitKey()
    cv2.destroyAllWindows()

def mat_op3():
    img1 = cv2.imread("cat.bmp")
    
    if img1 is None:
        print("Image load failed!")
        return
    

    img2 = img1[120:360, 220:560]
    img2 = cv2.bitwise_not(img2)
     
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
     
    cv2.waitKey()
    cv2.destroyAllWindows()

def mat_op4():
    mat1 = np.zeros((3, 4), dtype=np.int32)

    for j in range(mat1.shape[0]):
        for i in range(mat1.shape[1]):
            mat1[j, i] += 1

    for j in range(mat1.shape[0]):
        p = mat1[j, :]
        p += 1

    for value in np.nditer(mat1, op_flags=['readwrite']):
        value += 1

    print("mat1:\n", mat1)

def mat_op5():
    img1 = cv2.imread("lenna.bmp")

    print("Width:", img1.shape[1])
    print("Height:", img1.shape[0])
    print("Channels:", img1.shape[2])

    if img1.shape[2] == 1:
        print("img1 is a grayscale image.")
    elif img1.shape[2] == 3:
        print("img1 is a truecolor image.")

    data = np.array([2.0, 1.414, 3.0, 1.732], dtype=np.float32)
    mat1 = np.reshape(data, (2, 2))
    print("mat1:\n", mat1)

    cv2.imshow("img1", img1)
    cv2.waitKey()
    cv2.destroyAllWindows()



def mat_op7():
    img1 = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
    img1 = img1.astype(np.float32)

    data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float32)
    mat1 = np.reshape(data1, (3, 4))
    mat2 = mat1.reshape(1,12)

    print("mat1:\n", mat1)
    print("mat2:\n", mat2)

    mat3 = np.full((2,4),100)
    mat1 = np.vstack((mat1, mat3))
    print("mat1:\n", mat1)

    mat4 = np.full((1,4),255)
    mat1 = np.vstack((mat1, mat4))
    print("mat1:\n", mat1)


    cv2.imshow("img1", img1)
    cv2.waitKey()
    cv2.destroyAllWindows()

mat_op1()
mat_op2()
mat_op3()
mat_op5()
mat_op7()
