"""координаты вектора — это его проекции на соответствующие координатные оси"""
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
        return "Vector: ({}, {}, {})".format(self.__x, self.__y, self.__z)

    @property
    def pr_x(self):
        return self.__x

    @pr_x.setter
    def pr_x(self, x):
        self.__x = x

    @property
    def pr_y(self):
        return self.__y

    @pr_y.setter
    def pr_y(self, y):
        self.__y = y

    @property
    def pr_z(self):
        return self.__z

    @pr_z.setter
    def pr_z(self, z):
        self.__z = z

    def len_vector(self):
        """Method calculates vector length"""
        return round(math.sqrt(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2)), 2)

    def scalar_Product(self, other):
        x = self.__x * other.__x
        y = self.__y * other.__x
        z = self.__z * other.__x
        return x + y + z

    def cross_Product(self, other):
        x = self.__y * other.__z - self.__z * other.__y
        y = self.__z * other.__x - self.__x * other.__z
        z = self.__x * other.__y - self.__y * other.__x
        return Vector(x, y, z)

    def angle(self, other):
        a = self.scalar_Product(other)
        b = self.len_vector() * other.len_vector()
        return round(a / b, 2)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f'X-axis projection: {v1.pr_x}\nY-axis projection: '
          f'{v1.pr_y}\nZ-axis projection: {v1.pr_z}')
    print(f"Len vector: {v1.len_vector()}")
    print(v1 + v2)
    print(v1 - v2)
    print(f"Scalar product of vectors: {v1.scalar_Product(v2)}")
    print(f"Cross product of vectors: {v1.cross_Product(v2)}")
    print(f"Angle between vectors: {v1.angle(v2)}")
