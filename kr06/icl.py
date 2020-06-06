from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass


class Pyramid(Shape):

    def __init__(self, s, h):
        self.s = float(s)
        self.h = float(h)

    def get_volume(self):
        if self.s >= 0 and self.s * self.h >= 0:
            return self.s * self.h / 3
        else:
            raise ValueError


class SolidOfRevolution(Shape):

    pi = 3.14

    def __init__(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass


class Ball(SolidOfRevolution):

    def __init__(self, r):
        self.r = float(r)

    def get_volume(self):
        if self.r >= 0:
            return self.r ** 3 * 4 / 3 * self.pi
        else:
            raise ValueError


class Cylinder(SolidOfRevolution):

    def __init__(self, r, h):
        self.r = float(r)
        self.h = float(h)

    def get_volume(self):

        if self.r >= 0 and self.r * self.h >= 0:
            return self.pi * 2 * self.r * self.h
        else:
            raise ValueError


class Box(Shape):

    shapes = []

    def __init__(self, vol):
        self.mem = []
        self.vol = float(vol)

    def get_volume(self):
        if self.mem == []:
            return self.vol
        else:
            u = self.vol
            for a in self.mem:
                u -= a
            return u

    def add(self, shape):
        if (sum(self.mem) + shape.get_volume() - self.vol) < 0:
            self.mem.append(shape.get_volume())
            self.shapes.append(shape)
        else:
            raise ValueError


ball = Ball(1)
pyr=Pyramid(1,1)
print(ball.get_volume()) # 33.51
print(pyr.get_volume())
box = Box(20)
print(box.get_volume()) # 0
box.add(pyr)
print(box.get_volume())
box.add(ball)
print(box.get_volume())
print(box.shapes)