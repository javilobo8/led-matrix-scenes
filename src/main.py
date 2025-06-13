import time
import json
import argparse
from rgbmatrix import RGBMatrix
from matrix_options import GetOptions
from scene_manager import SceneManager
from scene import load_scenes_from_json

def main():
    parser = argparse.ArgumentParser(description="RGB Matrix Framework")
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Path to the scene config JSON file"
    )
    args = parser.parse_args()

    options = GetOptions()
    matrix = RGBMatrix(options=options)

    scenes = load_scenes_from_json(args.config)
    manager = SceneManager(scenes)
    manager.run(matrix, fps=120)

if __name__ == "__main__":
    main()


