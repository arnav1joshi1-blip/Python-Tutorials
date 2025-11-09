#Q1
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        print(f"Distance={math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)}")

    def midpoint(self, other):
        print(f"Midpoint=({(self.x + other.x) / 2},{(self.y + other.y) / 2})")

    def line_equation(self, other):
        m = (other.y - self.y) / (other.x - self.x)
        c = self.y - m * self.x
        print(f"y={m}x+{c}")

    def reflect_over_line(self, A, B):
        a = B.y - A.y
        b = A.x - B.x
        c = a * A.x + b * A.y
        d = (a * self.x + b * self.y - c) / (a**2 + b**2)
        rx = self.x - 2 * a * d
        ry = self.y - 2 * b * d
        print(f"Reflection=({rx},{ry})")
A = Point(1, 2)
B = Point(3, 4)
C = Point(5, 6)
Point.distance(A,B)
Point.midpoint(A,B)
Point.line_equation(A,B)
Point.reflect_over_line(C,A,B)
#Q2
from Vector_calculations import Vector
A = Vector(7, 8)
B = Vector(9, 10)
C = Vector(11, 12)
Vector.add(A, B, C)
Vector.magnitude(A)
Vector.magnitude(B)
Vector.magnitude(C)
Vector.dot(A, B)
Vector.dot(A, C)
Vector.dot(B, C)
Vector.angle(A, B)
Vector.angle(A, C)
Vector.angle(B, C)
Vector.projection(A, B)
#Q3
import math

class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, start, end):
        d = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
        print(f"Segment Length={d}")

    def closest_point(self, start, end, point):
        sx, sy = start.x, start.y
        ex, ey = end.x, end.y
        px, py = point.x, point.y
        t = ((px - sx)*(ex - sx) + (py - sy)*(ey - sy)) / ((ex - sx)**2 + (ey - sy)**2)
        t = max(0, min(1, t))
        cx = sx + t * (ex - sx)
        cy = sy + t * (ey - sy)
        print(f"Closest Point=({cx},{cy})")

    def point_to_segment_distance(self, start, end, point):
        sx, sy = start.x, start.y
        ex, ey = end.x, end.y
        px, py = point.x, point.y
        t = ((px - sx)*(ex - sx) + (py - sy)*(ey - sy)) / ((ex - sx)**2 + (ey - sy)**2)
        t = max(0, min(1, t))
        cx = sx + t * (ex - sx)
        cy = sy + t * (ey - sy)
        dist = math.sqrt((cx - px)**2 + (cy - py)**2)
        print(f"Distance from P to Segment={dist}")

S = Segment(13, 14)
E = Segment(15, 16)
P = Segment(17, 18)
obj = Segment(0, 0)
obj.distance(S, E)
obj.closest_point(S, E, P)
obj.point_to_segment_distance(S, E, P)
#Q4
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def intersection(self, other):
        det = self.a * other.b - other.a * self.b

        if det == 0:
            print("Lines are parallel or coincident.")
        else:
            x = (self.c * other.b - other.c * self.b) / det
            y = (self.a * other.c - other.a * self.c) / det
            print(f"Intersection Point=({x},{y})")
L1 = Line(19, 20, 21)
L2 = Line(21, 22, 23)
Line.intersection(L1, L2)
