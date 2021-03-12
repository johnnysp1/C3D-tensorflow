import cv2

#cap = cv2.VideoCapture('/c3d2/C3D-Action-Recognition/datasets/ucf-101/ApplyEyeMakeup/ApplyEyeMakeup_g10_c03.avi')
cap = cv2.VideoCapture('ApplyEyeMakeup_g10_c03.avi')

print(cap.isOpened())
ret, frame = cap.read()
print(ret)
#sudo cp <path to opencv source repo>/build/lib/python3/cv2.cpython-35m-x86_64-linux-gnu.so /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
img = cv2.imread('image.jpg')
print(img.shape)
