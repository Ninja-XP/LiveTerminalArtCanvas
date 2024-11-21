import random

class Animation:
    @staticmethod
    def rain_effect(canvas, num_drops=5):
        for _ in range(num_drops):
            x = random.randint(0, canvas.width - 1)
            y = random.randint(0, canvas.height - 1)
            canvas.draw(x, y, "|", color=4)
