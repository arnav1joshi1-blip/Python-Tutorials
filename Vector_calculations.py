import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v2, v3):
        rx = self.x + v2.x + v3.x
        ry = self.y + v2.y + v3.y
        print(f"Resultant=({rx},{ry})")

    def magnitude(self):
        mag = math.sqrt(self.x**2 + self.y**2)
        print(f"Magnitude={mag}")

    def dot(self, other):
        dot_val = self.x * other.x + self.y * other.y
        print(f"Dot Product={dot_val}")

    def angle(self, other):
        dot_val = self.x * other.x + self.y * other.y
        mag1 = math.sqrt(self.x**2 + self.y**2)
        mag2 = math.sqrt(other.x**2 + other.y**2)
        angle = math.degrees(math.acos(dot_val / (mag1 * mag2)))
        print(f"Angle={angle}")

    def projection(self, other):
        dot_val = self.x * other.x + self.y * other.y
        mag2 = math.sqrt(other.x**2 + other.y**2)
        factor = dot_val / (mag2**2)
        px = factor * other.x
        py = factor * other.y
        print(f"Projection=({px},{py})")