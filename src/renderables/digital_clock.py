from datetime import datetime
from rgbmatrix import graphics
from utils import parse_color, load_font
from renderables.base import Renderable

class DigitalClock(Renderable):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 85
        self.height = 35
        self.color = parse_color(color)
        self.font = load_font("src/assets/fonts/7_Seg_33x19.bdf")
        self.last_time = None
        self.cached_text = None

    def render(self, canvas, timestamp):
        current_time = datetime.now().strftime("%H:%M")

        if current_time != self.last_time:
            self.last_time = current_time
            self.cached_text = current_time

        x0, y0, w, h = self.x, self.y, self.width, self.height
        graphics.DrawLine(canvas, x0, y0, x0 + w - 1, y0, self.color)               # Top
        graphics.DrawLine(canvas, x0, y0 + h - 1, x0 + w - 1, y0 + h - 1, self.color) # Bottom
        graphics.DrawLine(canvas, x0, y0, x0, y0 + h - 1, self.color)               # Left
        graphics.DrawLine(canvas, x0 + w - 1, y0, x0 + w - 1, y0 + h - 1, self.color) # Right

        graphics.DrawText(canvas, self.font, x0 + 1, y0 + 1, self.color, self.cached_text)
