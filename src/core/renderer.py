import curses

class Renderer:
    @staticmethod
    def render_to_terminal(canvas, cursor_x, cursor_y, stdscr):
        stdscr.clear()
        char_grid = canvas.render()
        color_grid = canvas.get_color_grid()

        for y, row in enumerate(char_grid):
            for x, char in enumerate(row):
                color = color_grid[y][x]
                if x == cursor_x and y == cursor_y:
                    stdscr.addstr(y, x, "ʕ˖͜͡˖ʔ", curses.color_pair(color))
                else:
                    stdscr.addstr(y, x, char, curses.color_pair(color))
