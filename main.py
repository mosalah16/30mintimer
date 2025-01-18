import time
import tkinter as tk

import pygame

TARGET_DURATION = 1800


class Time:
    target_duration: int
    starting_time: int

    def __init__(self, target_duration: int) -> None:
        self.target_duration = target_duration
        self.starting_time = None

    def start(self) -> None:
        if self.starting_time is None:
            self.starting_time = int(time.monotonic())

    def reset(self) -> None:
        self.starting_time = None

    def _time_elapsed(self) -> int:
        return int(time.monotonic()) - self.starting_time

    def remaining_time(self) -> int:
        self.start()
        return self.target_duration - self._time_elapsed()

    @staticmethod
    def format_remaining_time(remaining_time: int) -> None:
        mins = remaining_time // 60
        secs = remaining_time % 60
        return f"{mins:02}:{secs:02}"


class Counter:
    def __init__(self, target_duration: int, widget: tk.Label) -> None:
        self.target_duration = target_duration
        self.time = Time(target_duration)
        self.widget = widget

    def reset(self) -> None:
        self.time.reset()

    def stop(self) -> None:
        pygame.mixer.music.load("assets/Kalimba.mp3")
        pygame.mixer.music.play()

    def update(self) -> None:
        remaining_time = self.time.remaining_time()
        formatted_remaining_time = self.time.format_remaining_time(remaining_time)
        self.widget.config(text=formatted_remaining_time)
        if remaining_time == 0:
            self.stop()
        else:
            root.after(100, self.update)


if __name__ == "__main__":
    pygame.mixer.init()

    root = tk.Tk()
    root.title("Timer")

    counter_widget = tk.Label(root, text=Time.format_remaining_time(TARGET_DURATION))
    counter_widget.grid(row=3)

    counter = Counter(target_duration=TARGET_DURATION, widget=counter_widget)

    starting_button = tk.Button(root, text="start", command=counter.update, width=5)
    starting_button.grid(row=2)

    reset_button = tk.Button(root, text="start", command=counter.reset, width=5)
    reset_button.grid(row=1)

    root.mainloop()
