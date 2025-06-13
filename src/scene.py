import json
from renderables.static_text import StaticText
from renderables.scrolling_text import ScrollingText
from renderables.image_element import ImageElement
from renderables.video import Video
from renderables.digital_clock import DigitalClock

class Scene:
    def __init__(self, duration, elements):
        self.duration = duration
        self.elements = elements
        print(f"Created scene with duration {self.duration} and {len(self.elements)} elements")

    def render(self, canvas, timestamp):
        for el in self.elements:
            el.render(canvas, timestamp)

def load_scenes_from_json(path):
    with open(path) as f:
        data = json.load(f)

    scenes = []
    for scene_data in data:
        elements = []
        for el in scene_data["elements"]:
            if el["type"] == "StaticText":
                elements.append(StaticText(el["text"], el["x"], el["y"], el["color"], el["font"]))
            elif el["type"] == "ScrollingText":
                elements.append(ScrollingText(el["text"], el["y"], el["color"], el["font"], el.get("speed", 1)))
            elif el["type"] == "Image":
                elements.append(ImageElement(el["path"], el.get("x", 0), el.get("y", 0), el.get("width", 100), el.get("height", 100)))
            elif el["type"] == "Video":
                elements.append(Video(el["folder"], el.get("fps", 15)))
            elif el["type"] == "DigitalClock":
                elements.append(DigitalClock(el["x"], el["y"], el["color"], el["font"]))
        scenes.append(Scene(scene_data["duration"], elements))

    return scenes