import time
from renderables.static_text import StaticText

class DigitalClock(StaticText):
    def __init__(self, x, y, color, font_path):
        super().__init__("", x, y, color, font_path)

    def render(self, canvas, timestamp):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        self.text = current_time
        super().render(canvas, timestamp)