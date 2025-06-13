import glob
from PIL import Image
from renderables.base import Renderable

class Video(Renderable):
    def __init__(self, folder, fps=15):
        self.frames = sorted(glob.glob(f"{folder}/*.png"))
        self.fps = fps

    def render(self, canvas, timestamp):
        index = int(timestamp * self.fps) % len(self.frames)
        img = Image.open(self.frames[index]).convert("RGB")
        canvas.SetImage(img, 0, 0)