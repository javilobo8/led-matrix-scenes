import os
from rgbmatrix import graphics
from renderables.base import Renderable
from utils import parse_color, load_font
from colors import COLOR_BLACK

class StaticText(Renderable):
    def __init__(self, text, x, y, color, font_name, outline=None):
        self.text = text
        self.x = x
        self.y = y
        self.color = parse_color(color)
        self.font = load_font(os.path.join("src", "assets", "fonts", f"{font_name}.bdf"))
        self.outline = parse_color(outline) if outline else None
        self.text_width = None

    def draw_outline(self, canvas, x, y):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    graphics.DrawText(canvas, self.font, x + dx, y + dy, self.outline, self.text)

    def render(self, canvas, timestamp):
        x = (canvas.width - self.get_text_width(canvas)) // 2 if self.x == "center" else int(self.x)
        if self.outline:
            self.draw_outline(canvas, x, self.y)
        graphics.DrawText(canvas, self.font, x, self.y, self.color, self.text)

    def get_text_width(self, canvas):
        if self.text_width is None:
            # Calculate once, cached for performance
            self.text_width = graphics.DrawText(canvas, self.font, -9999, -9999, COLOR_BLACK, self.text)
        return self.text_width
