import json

class FileManager:
    @staticmethod
    def save_canvas(canvas, file_name="drawing.json"):
        with open(file_name, "w") as f:
            json.dump(canvas.grid, f)

    @staticmethod
    def load_canvas(canvas, file_name="drawing.json"):
        try:
            with open(file_name, "r") as f:
                canvas.grid = json.load(f)
        except FileNotFoundError:
            print(f"File {file_name} not found!")
