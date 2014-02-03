from object import Object

class Player(Object):
    def __init__(self, x, y, dx=0, dy=0):
        Object.__init__(self, x, y, dx, dy)
