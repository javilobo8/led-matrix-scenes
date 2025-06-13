import time

class SceneManager:
    def __init__(self, scenes):
        self.scenes = scenes
        self.current = 0

    def run(self, matrix, fps=30):
        canvas = matrix.CreateFrameCanvas()
        frame_duration = 1.0 / fps

        while True:
            scene = self.scenes[self.current]
            start = time.time()

            while time.time() - start < scene.duration:
                frame_start = time.time()
                canvas.Clear()
                scene.render(canvas, time.time() - start)
                canvas = matrix.SwapOnVSync(canvas)
                time.sleep(max(0, frame_duration - (time.time() - frame_start)))

            self.current = (self.current + 1) % len(self.scenes)