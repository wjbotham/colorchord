from object import Object

class Bullet(Object):
    def __init__(self, source_x, source_y, target_x, target_y, speed=1):
        if target_x == source_x and target_y == source_y:
            target_x += 1
        dist_x = target_x - source_x
        dist_y = target_y - source_y
        dist = (dist_x**2 + dist_y**2)**0.5
        Object.__init__(self, source_x, source_y, dist_x/dist*speed, dist_y/dist*speed)
