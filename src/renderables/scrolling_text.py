from rgbmatrix import graphics
from renderables.base import Renderable
from utils import parse_color, load_font
from colors import COLOR_BLACK

loaded_fonts = {}

def load_and_cache_font(font_path):
    if font_path not in loaded_fonts:
        loaded_fonts[font_path] = graphics.Font()
        loaded_fonts[font_path].LoadFont(font_path)
    return loaded_fonts[font_path]

class ScrollingText(Renderable):
    def __init__(self, text, y, color, font_path, speed=1):
        self.text = text
        self.y = y
        self.color = parse_color(color)
        self.font = load_and_cache_font(font_path)
        self.speed = speed

    def render(self, canvas, timestamp):
        self.text_width = graphics.DrawText(canvas, self.font, -10, -10, COLOR_BLACK, self.text)
        x = int(canvas.width - (timestamp * self.speed * 10)) % (self.text_width + canvas.width)
        graphics.DrawText(canvas, self.font, x, self.y, self.color, self.text)