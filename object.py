class Object:
    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def tick(self):
        self.x += self.dx
        self.y += self.dy

    def get_position(self):
        return (round(self.x), round(self.y))
    position = property(get_position)
