class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otherVector):
        return Vector(self.x + otherVector.x, self.y + otherVector.y)

    def __repr__(self):
        return f"X:{self.x}, Y:{self.y}"

    def __call__(self, *args, **kwargs):
        print(f"Hello, I was called.")
        print(V3)

    def __del__(self):
        print("Object is being deconstructed!")


V1 = Vector(10, 20)
V2 = Vector(50, 60)
V3 = V2 + V1
V3()
