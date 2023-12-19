from tkinter import *
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time = user_input.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error Message", "Please Enter Value")
    else:
        while True:
            time.sleep(1)
            current_time = time.strftime("%H:%M")
            if alarm_time == current_time:
                playmusic()

def playmusic():
    mixer.init()
    mixer.music.load('clock.mp3')
    mixer.music.play()

    stop_button = Button(box2, text="Stop", font=('Arial Narrow', 16, 'bold'), command=stop_music)
    stop_button.grid(row=2, column=1)

    snooze_button = Button(box2, text="Snooze", font=('Arial Narrow', 16, 'bold'), command=snooze_alarm)
    snooze_button.grid(row=2, column=3)

    while mixer.music.get_busy():
        root.update()
        time.sleep(1)

def stop_music():
    mixer.music.stop()
    sys.exit()

def snooze_alarm():
    mixer.music.stop()
    snooze_time = 300  # snooze for 5 minutes (adjust as needed)
    time.sleep(snooze_time)
    playmusic()

root = Tk()
root.title("Alarm Clock")
root.geometry("600x380")

canvas = Canvas(root, width=600, height=380)
image = ImageTk.PhotoImage(Image.open("flower.png"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

header = Frame(root)
box1 = Frame(root)
box1.place(x=250, y=180)
box2 = Frame(root)
box2.place(x=250, y=260)

user_input = Entry(box1, font=('Arial Narrow', 20), width=8)
user_input.grid(row=0, column=2)

start_button = Button(box2, text="Set Alarm", font=('Arial Narrow', 16, 'bold'), command=alarm)
start_button.grid(row=2, column=2)

root.mainloop()