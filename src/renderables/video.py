import cv2
from PIL import Image
from renderables.base import Renderable

class Video(Renderable):
    def __init__(self, video_path, fps=15, x=0, y=0, width=None, height=None):
        self.cap = cv2.VideoCapture(video_path)
        self.video_fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.video_fps

        self.fps = fps
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, canvas, timestamp):
        video_time = timestamp % self.duration
        frame_index = int(video_time * self.video_fps)

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        success, frame = self.cap.read()
        if not success:
            return  # skip if failed

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        # Resize if width/height specified
        if self.width and self.height:
            img = img.resize((self.width, self.height), Image.Resampling.NEAREST)

        canvas.SetImage(img, self.x, self.y)
