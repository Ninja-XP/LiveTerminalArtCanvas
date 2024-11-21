class Canvas:
    def __init__(self, width=50, height=20, default_char=".", default_color=0):
        self.width = width
        self.height = height
        self.default_char = default_char
        self.default_color = default_color
        self.grid = [[(default_char, default_color) for _ in range(width)] for _ in range(height)]

    def draw(self, x, y, char, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = (char, color)

    def clear(self):
        self.grid = [[(self.default_char, self.default_color) for _ in range(self.width)] for _ in range(self.height)]

    def render(self):
        return [[char for char, _ in row] for row in self.grid]

    def get_color_grid(self):
        return [[color for _, color in row] for row in self.grid]
