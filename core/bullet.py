from core.object import Object

class Bullet(Object):
    def __init__(self, source, target_x, target_y, speed, life):
        if target_x == source.x and target_y == source.y:
            target_x += 1
        dist_x = target_x - source.x
        dist_y = target_y - source.y
        dist = (dist_x**2 + dist_y**2)**0.5
        dx = dist_x/dist*speed + source.dx
        dy = dist_y/dist*speed + source.dy
        Object.__init__(self, source.x, source.y, dx, dy, life)
