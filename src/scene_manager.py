import time
import threading

class SceneManager:
    def __init__(self, matrix, fps=30):
        self.matrix = matrix
        self.fps = fps
        self.canvas = matrix.CreateFrameCanvas()
        self.running = threading.Event()
        self.scenes = []
        self.current = 0
        self.lock = threading.Lock()
        self.updated = threading.Event()

    def load_scenes(self, scenes):
        with self.lock:
            self.scenes = scenes
            self.current = 0
            self.updated.set()  # Interrumpe la escena actual
            self.running.set()  # Asegura que el render loop esté corriendo

    def run(self):
        self.running.set()
        while True:
            self.running.wait()

            with self.lock:
                if not self.scenes:
                    time.sleep(0.1)
                    continue
                scene = self.scenes[self.current]
                self.updated.clear()

            start = time.time()
            if scene.duration == 0:
                while self.running.is_set() and not self.updated.is_set():
                    self._render_scene(scene, time.time() - start)
            else:
                while (time.time() - start < scene.duration 
                       and self.running.is_set() 
                       and not self.updated.is_set()):
                    self._render_scene(scene, time.time() - start)

                with self.lock:
                    if not self.updated.is_set():
                        self.current = (self.current + 1) % len(self.scenes)

    def _render_scene(self, scene, timestamp):
        frame_start = time.time()
        self.canvas.Clear()
        scene.render(self.canvas, timestamp)
        self.canvas = self.matrix.SwapOnVSync(self.canvas)
        time.sleep(max(0, 1.0 / self.fps - (time.time() - frame_start)))

    def stop(self):
        self.running.clear()
