from tkinter import *
import tkinter as tk
import time
import pygame

pygame.mixer.init()

def start():
    global t
    global starting_time
    if starting_time==0:
        starting_time=int(time.monotonic())
    
    current_time=int(time.monotonic())
    time_elapsed= int(current_time - starting_time)
    remaining_time=t-time_elapsed
    if remaining_time>0:
        mins=remaining_time//60
        secs=remaining_time%60
        ct=f'{mins:02}:{secs:02}'
        counter.config(text=ct)
        root.after(100,start)
    elif remaining_time==0:
        counter.config(text="00:00")
        pygame.mixer.music.load("Kalimba.mp3")
        pygame.mixer.music.play()
        
def change():
    global t
    x=changet.get()
    x=int(x)*60
    if x!=0:
        t=x
    elif x==0:
        t=1800
        
    


starting_time=0
t=1800

root = tk.Tk()
root.title("Timer")

txt=Label(root, text='By picking 0 you are setting it to a default 30 minutes')
txt.grid(row=1)


changet=IntVar()
changet=Spinbox(root, from_=0, to=120)
changet.grid(row=0, column=0)



counter=tk.Label(root, text="Pick your time in min and press start")
counter.grid(row=3)

starting_button = tk.Button(root, text="start", command=start, width=5)
starting_button.grid(row=2)
change_button = tk.Button(root, text="change", command=change, width=5)
change_button.grid(row=0, column=1)

root.mainloop()




