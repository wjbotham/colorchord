from object import Object
from math import sqrt

class Player(Object):
    def __init__(self, x, y, dx=0, dy=0):
        Object.__init__(self, x, y, dx, dy)
        self._w_down = False
        self._a_down = False
        self._s_down = False
        self._d_down = False

    def get_w_down(self):
        return self._w_down
    def set_w_down(self, w_down):
        self._w_down = bool(w_down)
        self._update_speed()
    w_down = property(get_w_down, set_w_down)

    def get_a_down(self):
        return self._a_down
    def set_a_down(self, a_down):
        self._a_down = bool(a_down)
        self._update_speed()
    a_down = property(get_a_down, set_a_down)

    def get_s_down(self):
        return self._s_down
    def set_s_down(self, s_down):
        self._s_down = bool(s_down)
        self._update_speed()
    s_down = property(get_s_down, set_s_down)

    def get_d_down(self):
        return self._d_down
    def set_d_down(self, d_down):
        self._d_down = bool(d_down)
        self._update_speed()
    d_down = property(get_d_down, set_d_down)

    def _update_speed(self):
        x_dir = self.d_down - self.a_down
        y_dir = self.s_down - self.w_down
        dx = 0
        dy = 0
        if x_dir == 0 and y_dir == 0:
            None
        elif x_dir != 0 and y_dir != 0:
            dx = x_dir * (1/sqrt(2))
            dy = y_dir * (1/sqrt(2))
        elif x_dir != 0:
            dx = x_dir
            dy = 0
        elif y_dir != 0:
            dx = 0
            dy = y_dir
        self.dx = dx
        self.dy = dy
