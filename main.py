# import statements
import cv2
import PIL
import tkinter as tk
import tkinter.font as font
from recording import recording
from motion import noise
from record import record
from PIL import Image, ImageTk
from tkinter import filedialog
from alarm import beep


# GUI 
window = tk.Tk()
window.title("Smart cctv System")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('900x600')

# frame
frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Security Camera System", bg= "black", fg= "White")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(7,7), column=2)
# icon images
icon = Image.open('icons/Icons-Camera.ico')
icon = icon.resize((150,150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.LANCZOS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/exit.png')
btn2_image = btn2_image.resize((50,50), Image.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/recording.png')
btn5_image = btn5_image.resize((50,50), Image.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)


# --------------- Button -------------------#
btn_font = font.Font(size=20)
btn1 = tk.Button(frame1, text='Monitoring', height=90, width=180, fg='green',command =beep, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=2, pady=(20,10))

btn2 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3)

btn_font = font.Font(size=20)
btn3 = tk.Button(frame1, text='Motion', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=3, pady=(20,10))

btn4 = tk.Button(frame1, text='Live Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=3, pady=(20,10), column=2)


btn5 = tk.Button(frame1, text="Recording", fg="orange",command=recording, compound='left', image=btn5_image, height=90, width=180)
btn5['font'] = btn_font
btn5.grid(row=2, column=2, pady=(20,10))


frame1.pack()
window.mainloop()


