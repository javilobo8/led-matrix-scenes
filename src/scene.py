import json
from renderables.static_text import StaticText
from renderables.scrolling_text import ScrollingText
from renderables.image_element import ImageElement
from renderables.video import Video
from renderables.digital_clock import DigitalClock
from renderables.rectangle import Rectangle
from renderables.countdown import CountDown
from renderables.notification import Notification

class Scene:
    def __init__(self, duration, elements):
        self.duration = duration
        self.elements = elements
        print(f"Created scene with duration {self.duration} and {len(self.elements)} elements")

    def render(self, canvas, timestamp):
        for el in self.elements:
            el.render(canvas, timestamp)

def _load_scenes_from_data(data):
    scenes = []
    for scene_data in data:
        elements = []
        for el in scene_data["elements"]:
            if el["type"] == "StaticText":
                elements.append(StaticText(el["text"], el["x"], el["y"], el["color"], el.get("font", "6x10"), el.get("outline", None)))
            elif el["type"] == "Notification":
                elements.append(Notification(el["text"], el["x"], el["y"], el["color"], el.get("font", "6x10"), el.get("outline", None), el.get("notification_color")))
            elif el["type"] == "ScrollingText":
                elements.append(ScrollingText(el["text"], el["y"], el["color"], el.get("font", "6x10"), el.get("speed", 1), el.get("x_start"), el.get("x_end"), el.get("pause_time")))
            elif el["type"] == "Image":
                elements.append(ImageElement(el["path"], el.get("x", 0), el.get("y", 0), el.get("width", 128), el.get("height", 128)))
            elif el["type"] == "Video":
                elements.append(Video(el["path"], el.get("fps", 15), el.get("x", 0), el.get("y", 0), el.get("width", 128), el.get("height", 128)))
            elif el["type"] == "DigitalClock":
                elements.append(DigitalClock(el["x"], el["y"], el["color"]))
            elif el["type"] == "Rectangle":
                elements.append(Rectangle(el["x"], el["y"], el["width"], el["height"], el["color"], el.get("fill", False)))
            elif el["type"] == "CountDown":
                elements.append(CountDown(el["x"], el["y"], el["color"], el.get("font", "6x10"), el.get("outline", None), el.get("target")))
        scenes.append(Scene(scene_data["duration"], elements))
    return scenes

def load_scenes_from_json(path):
    with open(path) as f:
        data = json.load(f)
    return _load_scenes_from_data(data)

def load_scenes_from_dict(data):
    # Espera que `data` sea una lista de escenas, como en el JSON
    return _load_scenes_from_data(data)
