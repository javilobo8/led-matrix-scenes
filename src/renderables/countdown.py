import time
from datetime import datetime
from renderables.static_text import StaticText

class CountDown(StaticText):
    def __init__(self, x, y, color, font_path, outline, target):
        super().__init__("", x, y, color, font_path, outline)
        # Parse target time from ISO String
        self.target_time = datetime.fromisoformat(target).timestamp()

    def get_countdown_text(self):
        remaining = self.target_time - time.time()
        if remaining <= 0:
            return "00d 00h 00m 00s"
        days = int(remaining // (24 * 3600))
        hours = int((remaining % (24 * 3600)) // 3600)
        minutes = int((remaining % 3600) // 60)
        seconds = int(remaining % 60)
        return f"{days:02}d {hours:02}h {minutes:02}m {seconds:02}s"

    def render(self, canvas, timestamp):
        self.text = self.get_countdown_text()
        super().render(canvas, timestamp)