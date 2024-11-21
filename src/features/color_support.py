import curses

def test_colors(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    for i in range(1, 5):
        stdscr.addstr(f"Color {i}\n", curses.color_pair(i))

    stdscr.getch()

curses.wrapper(test_colors)
