class Object:
    def __init__(self, x, y, dx=0, dy=0, life=None, light=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.life = life
        self.light = light
        self.needs_cleanup = False

    def get_life(self):
        return self._life_remaining
    def set_life(self, life):
        self._life_remaining = life
        if life != None and self._life_remaining <= 0:
            self.needs_cleanup = True
    life = property(get_life, set_life)

    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

    def tick(self):
        self.x += self.dx
        self.y += self.dy
        if self.life != None:
            self.life -= 1

    def get_position(self):
        return (round(self.x), round(self.y))
    position = property(get_position)
