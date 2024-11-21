import curses
class InputHandler:
    def __init__(self):
        self.cursor_x = 0
        self.cursor_y = 0

    def handle_input(self, canvas, key, color):
        if key == curses.KEY_UP:
            self.cursor_y = max(0, self.cursor_y - 1)
        elif key == curses.KEY_DOWN:
            self.cursor_y = min(canvas.height - 1, s>
        elif key == curses.KEY_LEFT:
            self.cursor_x = max(0, self.cursor_x - 1)
        elif key == curses.KEY_RIGHT:
            self.cursor_x = min(canvas.width - 1, se>
        elif key == ord(" "):
            canvas.draw(self.cursor_x, self.cursor_y>
        elif key == ord("c"):
            canvas.clear()
