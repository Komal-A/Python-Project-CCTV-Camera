from tkinter import filedialog
import cv2 
from tkVideoPlayer import TkinterVideo
from tkinter import filedialog
import tkinter as tk
import mttkinter
from PIL import ImageTk, Image

def noise():
    input_video_path = filedialog.askopenfilename(initialdir="C:\\University\\Year 3\\Media Technology CSY3010\\Term 2\\as1\\Recordings",title="Open File", filetypes=(("mp4 files", "*.mp4"), ("mp4 files", "*.*")))
    cap = cv2.VideoCapture(input_video_path)

    while cap.isOpened():
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        diff = cv2.absdiff(frame1, frame2)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5,5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow("esc. to exit", frame1)

        if cv2.waitKey(40) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
