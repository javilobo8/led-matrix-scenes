from rgbmatrix import graphics
from renderables.base import Renderable
from utils import parse_color, load_and_cache_font
from colors import COLOR_BLACK
import time
import os

class ScrollingText(Renderable):
    def __init__(self, text, y, color, font_name, speed=1, x_start=0, x_end=None, pause_time=0):
        self.text = text
        self.y = y
        self.color = parse_color(color)
        self.font = load_and_cache_font(os.path.join("src", "assets", "fonts", f"{font_name}.bdf"))
        self.speed = speed
        self.x_start = x_start
        self.x_end = x_end
        self.pause_time = pause_time

        self.text_width = None
        self.last_reset_time = time.time()
        self.scroll_x = 0
        self.waiting = False

    def render(self, canvas, timestamp):
        if self.text_width is None:
            self.text_width = graphics.DrawText(canvas, self.font, -1000, -1000, COLOR_BLACK, self.text)

        width = canvas.width if self.x_end is None else self.x_end - self.x_start

        if self.waiting:
            if time.time() - self.last_reset_time >= self.pause_time:
                self.scroll_x = 0
                self.last_reset_time = time.time()
                self.waiting = False
            return

        x_pos = self.x_start + width - self.scroll_x
        graphics.DrawText(canvas, self.font, x_pos, self.y, self.color, self.text)

        self.scroll_x += self.speed
        if self.scroll_x > self.text_width + width:
            self.waiting = self.pause_time > 0
            self.last_reset_time = time.time()
            if not self.waiting:
                self.scroll_x = 0
