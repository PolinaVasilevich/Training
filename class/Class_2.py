import math


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__x
        z = self.__z + other.__x
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y
        z = self.__z - other.__z
        return Vector(x, y, z)

    def __str__(self):
        return f"Vector: ({self.__x}, {self.__y}, {self.__z})"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z

    @staticmethod
    def length(self):
        return round(math.sqrt(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2)), 2)

    @staticmethod
    def scalar(first, second):
        x = first.__x * second.__x
        y = first.__y * second.__x
        z = first.__z * second.__x
        return x + y + z

    @staticmethod
    def cross(first, second):
        x = first.__y * second.__z - first.__z * second.__y
        y = first.__z * second.__x - first.__x * second.__z
        z = first.__x * second.__y - first.__y * second.__x
        return Vector(x, y, z)

    @classmethod
    def angle(cls, first, second):
        a = cls.scalar(first, second)
        b = abs(cls.length(first)) * abs(cls.length(second))
        return round(a / b, 2)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f'X-axis projection: {v1.x}\nY-axis projection: '
          f'{v1.y}\nZ-axis projection: {v1.z}')
    print(f"Length vector: {Vector.length(v1)}")
    print(f"Vector addition: {v1 + v2}")
    print(f"Vector subtraction: {v1 + v2}")
    print(f"Scalar product of vectors: {Vector.scalar(v1, v2)}")
    print(f"Vector product of vectors: {Vector.cross(v1, v2)}")
    print(f"Angle between vectors: {Vector.angle(v1, v2)}")
