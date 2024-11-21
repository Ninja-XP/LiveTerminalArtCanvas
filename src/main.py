import curses
from core.canvas import Canvas
from core.renderer import Renderer
from core.input_handler import InputHandler
from features.file_manager import FileManager
from features.animation import Animation

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    current_color = 1

    canvas = Canvas(width=50, height=20)
    renderer = Renderer()
    input_handler = InputHandler()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Live Terminal Art Canvas! Press Q to quit. Use 1-4 for colors, S to save, L to load, R for rain.")

        renderer.render_to_terminal(canvas, input_handler.cursor_x, input_handler.cursor_y, stdscr)

        key = stdscr.getch()
        if key == ord("q"):
            break
        elif key in (ord("1"), ord("2"), ord("3"), ord("4")):
            current_color = int(chr(key))
        elif key == ord("s"):
            FileManager.save_canvas(canvas)
        elif key == ord("l"):
            FileManager.load_canvas(canvas)
        elif key == ord("r"):
            Animation.rain_effect(canvas)
        else:
            input_handler.handle_input(canvas, key, current_color)

        stdscr.refresh()

curses.wrapper(main)
