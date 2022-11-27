# import streamlit as st
# from ffpyplayer.player import MediaPlayer
import cv2
import pyautogui
import numpy as np
import win32gui

from PIL import Image
def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''
    # Format_RGB32 = 4,存入格式为B,G,R,A 对应 0,1,2,3
    # RGB32图像每个像素用32比特位表示，占4个字节，
    # R，G，B分量分别用8个bit表示，存储顺序为B，G，R，最后8个字节保留
    incomingImage = incomingImage.convertToFormat(4)
    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    return np.array(ptr).reshape(height, width, 4)


# img = Image.open('test.jpg')
# o = img.resize((300,200))
# o.show()


# hwnd_title = {}

# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

# win32gui.EnumWindows(get_all_hwnd, 0)

# for h, t in hwnd_title.items():
#     if t!= "":
#         print(h, t)

# from PyQt5.QtWidgets import QApplication
# import win32gui
# import sys
# #这个是截取全屏的
# hwnd = win32gui.FindWindow(None, 'C:\work_spaces\opencv')
# app = QApplication(sys.argv)
# screen = QApplication.primaryScreen()
# img = screen.grabWindow(hwnd).toImage()
# cv2.imshow('dd',convertQImageToMat(img))
# img.save("screenshot.jpg")


# region=[300,50, 200, 100]# 分别代表：左上角坐标，宽高
# img = pyautogui.screenshot()  
# #对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
# #因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
# img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
# cv2.draw
# cv2.imshow("截屏",img)


# color_img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow("ss",color_img)

cap = cv2.VideoCapture("dji.mp4")



if cap.isOpened():
    open,frame = cap.read()
else:
    print("open failed")

while open:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(frame.shape[1]//2,(frame.shape[0]//2)))

    # frame = frame[0:500,250:500]
   
    cv2.imshow("fpv",frame)
    if cv2.waitKey(5) & 0xff == 27:
        break

cv2.waitKey(0)

