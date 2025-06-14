from rgbmatrix import graphics
from renderables.base import Renderable
from utils import parse_color, load_font
from colors import COLOR_BLACK

class Rectangle(Renderable):
    def __init__(self, x, y, width, height, color, fill):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = parse_color(color)
        self.fill = fill

    def render(self, canvas, timestamp):
        # Optionally fill the rectangle
        if self.fill:
            for y in range(self.y, self.y + self.height):
                graphics.DrawLine(canvas, self.x, y, self.x + self.width - 1, y, self.color)
        else:
            graphics.DrawLine(canvas, self.x, self.y, self.x + self.width - 1, self.y, self.color)
            graphics.DrawLine(canvas, self.x, self.y + self.height - 1, self.x + self.width - 1, self.y + self.height - 1, self.color)
            graphics.DrawLine(canvas, self.x, self.y, self.x, self.y + self.height - 1, self.color)
            graphics.DrawLine(canvas, self.x + self.width - 1, self.y, self.x + self.width - 1, self.y + self.height - 1, self.color)