import argparse
import threading
import json
from flask import Flask, request, jsonify
from rgbmatrix import RGBMatrix
from matrix_options import GetOptions
from scene import load_scenes_from_json, load_scenes_from_dict
from scene_manager import SceneManager

app = Flask(__name__)
manager = None  # Se inicializa en main()

@app.route("/update", methods=["POST"])
def update_scenes():
    try:
        data = request.get_json()
        new_scenes = load_scenes_from_dict(data)
        manager.load_scenes(new_scenes)
        return "OK"
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def start_flask():
    app.run(host="0.0.0.0", port=8000)

def main():
    global manager
    parser = argparse.ArgumentParser(description="RGB Matrix Framework")
    parser.add_argument("--config", type=str, default="config.json", help="Path to scene config JSON")
    args = parser.parse_args()

    options = GetOptions()
    matrix = RGBMatrix(options=options)

    initial_scenes = load_scenes_from_json(args.config)
    manager = SceneManager(matrix, fps=60)
    manager.load_scenes(initial_scenes)

    t1 = threading.Thread(target=manager.run, daemon=True)
    t2 = threading.Thread(target=start_flask, daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
