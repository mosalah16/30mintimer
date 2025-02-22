import time
import tkinter as tk
from pathlib import Path
import sys
import os

from pygame.mixer import Sound
from pygame.mixer import init as init_pygame_mixer

DEFAULT_TARGET_DURATION = 1800


def resource_path(relative_path: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(os.path.join(sys._MEIPASS, relative_path))
    return Path(relative_path)

PATH_TO_MUSIC = resource_path("assets/Kalimba.mp3")

class Time:
    target_duration: int
    starting_time: int

    def __init__(self, target_duration: int) -> None:
        self.target_duration = target_duration
        self.starting_time = None

    def _set_starting_time(self) -> None:
        if self.starting_time is None:
            self.starting_time = int(time.monotonic())

    def update_target_duration(self, new_time: int) -> None:
        self.target_duration = new_time

    def reset(self) -> None:
        self.starting_time = None

    def _time_elapsed(self) -> int:
        self._set_starting_time()
        return int(time.monotonic()) - self.starting_time

    def remaining_time(self) -> int:
        return self.target_duration - self._time_elapsed()


class Counter:
    def __init__(self, target_duration: int, widget: tk.Label) -> None:
        self.target_duration = target_duration
        self.widget = widget
        self.time = Time(target_duration)
        init_pygame_mixer()
        self.sound = Sound(PATH_TO_MUSIC)
        

    def reset(self) -> None:
        self.sound.stop()
        self.time.reset()

    def change(self) -> None:
        new_target_duration = (int(change_time.get())) * 60
        self.time.update_target_duration(new_target_duration)
        self.reset()
        self.update_display_remaining_time(new_target_duration)

    def run(self):
        remaining_time = self.time.remaining_time()
        self.update_display_remaining_time(remaining_time)
        if remaining_time == 0:
            self.finish()
        else:
            root.after(100, self.run)

    def finish(self) -> None:
        self.sound.play()

    def update_display_remaining_time(self, new_time: int) -> None:
        new_time = self.format_remaining_time(new_time)
        self.widget.config(text=new_time)

    @staticmethod
    def format_remaining_time(remaining_time: int) -> None:
        mins = remaining_time // 60
        secs = remaining_time % 60
        return f"{mins:02}:{secs:02}"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Timer")

    counter_widget = tk.Label(
        root, text=Counter.format_remaining_time(DEFAULT_TARGET_DURATION)
    )
    counter_widget.grid(row=1)

    counter = Counter(target_duration=DEFAULT_TARGET_DURATION, widget=counter_widget)

    change_time = tk.IntVar()
    change_time = tk.Spinbox(root, from_=1, to=10000, state="readonly")
    change_time.grid(row=0)

    starting_button = tk.Button(root, text="start", command=counter.run, width=5)
    starting_button.grid(row=2)

    reset_button = tk.Button(root, text="reset", command=counter.reset, width=5)
    reset_button.grid(row=3)

    change_button = tk.Button(root, text="change", command=counter.change, width=5)
    change_button.grid(row=4)

    root.mainloop()
