import time
from rgbmatrix import graphics
from datetime import datetime
from renderables.static_text import StaticText
from utils import parse_color

class Notification(StaticText):
    def __init__(self, text, x, y, color, font_path, outline, notification_color):
        super().__init__(text, x + 8, y, color, font_path, outline)
        self.notification_color = parse_color(notification_color)

    def render(self, canvas, timestamp):
        offset = 4
        x = self.x - offset
        graphics.DrawLine(canvas, x - 4, self.y - 8, x - 4, self.y, self.notification_color)
        graphics.DrawLine(canvas, x - 3, self.y - 8, x - 3, self.y, self.notification_color)
        graphics.DrawLine(canvas, x - 2, self.y - 8, x - 2, self.y, self.notification_color)
        graphics.DrawLine(canvas, x - 1, self.y - 8, x - 1, self.y, self.notification_color)
        super().render(canvas, timestamp)