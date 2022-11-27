# import streamlit as st
# from ffpyplayer.player import MediaPlayer
import cv2


# color_img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow("ss",color_img)

vc = cv2.VideoCapture("dji.mp4")

if vc.isOpened():
    open,frame = vc.read()
else:
    print("open failed")

while open:
    ret,frame = vc.read()
    
    # cut = frame[10:200,0:frame.shape[1]]
    cv2.imshow("fpv",frame)
    if cv2.waitKey(5) & 0xff == 27:
        break

cv2.waitKey(0)