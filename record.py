import time
import cv2
from datetime import datetime

def record():
    cap = cv2.VideoCapture(0)

# creating haadcascades to identify faces and bodies in a real time video
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_fullbody.xml")

# declaring Variables
    detection = False
    detection_stopped_time = None
    timer_started = False
    Record_after_detection = 5

# getting frame size
    frame_size = (int(cap.get(3)), int(cap.get(4)))
# creating four character code which is kind of a video format
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")


    while True:
    # capture a frame
        _, frame = cap.read()
    # created a frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 2)

    # if statement to check if we have face or body in the frame 
        if len(faces) + len(bodies) > 0:
            if detection:
                timer_started = False
            else:
                detection = True
                current_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"Recordings/{current_time}.mp4", fourcc, 20, frame_size)
                print("Recording Started!")

        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= Record_after_detection:
                    detection = False
                    timer_started = False
                    out.release()
                    print("Recording Stopped!")
                    cv2.destroyWindow("esc. to exit")
            else:
                timer_started = True
                detection_stopped_time = time.time()
               

       # recording = True
        if detection:
            out.write(frame)

# This will draw a rectangle around the face 
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
        for (x, y, width, height) in bodies:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

        cv2.imshow("esc. to exit", frame)
    
        if cv2.waitKey(1) == 27:
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()