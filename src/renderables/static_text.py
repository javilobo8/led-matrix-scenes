from rgbmatrix import graphics
from renderables.base import Renderable
from utils import parse_color, load_font
from colors import COLOR_BLACK

class StaticText(Renderable):
    def __init__(self, text, x, y, color, font_path):
        self.text = text
        self.x = x
        self.y = y
        self.color = parse_color(color)
        self.font = load_font(font_path)

    def render(self, canvas, timestamp):
        x = 0
        if self.x == "center":
            text_width = graphics.DrawText(canvas, self.font, -10, -10, COLOR_BLACK, self.text)
            x = (canvas.width - text_width) // 2
        else:
            x = int(self.x)
        graphics.DrawText(canvas, self.font, x, self.y, self.color, self.text)