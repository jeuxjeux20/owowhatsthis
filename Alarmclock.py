from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox

root = Tk()
root.title("Alarm Clock")
def SubmitButton():
    AlarmTime= entry1.get()
    CurrentTime = time.strftime("%H:%M")
    print("Alarm will ring at: {}".format(AlarmTime))
    while AlarmTime != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime == CurrentTime:
        os.system("start Alarm.mp3")
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)

label1= ttk.Label(frame1,text = "Enter the Alarm time:")
label1.pack()

entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()

button1= ttk.Button(frame1, text= "Submit", command=SubmitButton)
button1.pack()

root.mainloop()
