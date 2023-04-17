import cv2
import tkinter as tk
from PIL import ImageTk, Image
from tkVideoPlayer import TkinterVideo
from tkinter import filedialog
import numpy as np
import datetime

def recording():
    cap = cv2.VideoCapture('nv232.MOV')
    _, frame1 = cap.read()
    _, frame2 = cap.read()


    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contr in contr:
            x,y,w,h = cv2.boundingRect(contr)

        #
            if cv2.contourArea(contr) < 900:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "Un-Authorised person", (300, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow("esc. to exit", frame1)
        frame1 = frame2
        _, frame2 = cap.read()

    
        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
