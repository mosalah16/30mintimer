import tkinter as tk
import time
def start():
    global t
    if t>1:
        t=t-1
        min=t//60
        sec=t%60
        ct = f"{min:02}:{sec:02}"
        counter.config(text=ct)
        root.after(1000,start)
        


t=1800

root = tk.Tk()
root.title("Timer")

counter=tk.Label(root, text="30:00")
counter.pack(pady=100,padx=100)

starting_button = tk.Button(root, text="start", command=start, width=10)
starting_button.pack(pady=5)

root.mainloop()




