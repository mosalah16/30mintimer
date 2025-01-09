import tkinter as tk
import time
def start():
    global t
    global starting_time
    if starting_time==0:
        starting_time=time.time()
    
    current_time=time.time()
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
        
    


starting_time=0
t=1799

root = tk.Tk()
root.title("Timer")

counter=tk.Label(root, text="30:00")
counter.pack(pady=100,padx=100)

starting_button = tk.Button(root, text="start", command=start, width=10)
starting_button.pack(pady=5)

root.mainloop()




