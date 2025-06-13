from PIL import Image
from renderables.base import Renderable

class ImageElement(Renderable):
    def __init__(self, path, x=0, y=0, width=100, height=100):
        self.image = Image.open(path).convert("RGB")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if self.width is not None and self.height is not None:
            self.image = self.image.resize((self.width, self.height), Image.Resampling.BILINEAR)

    def render(self, canvas, timestamp):
        canvas.SetImage(self.image, self.x, self.y)