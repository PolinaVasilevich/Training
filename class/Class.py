import math


class Vector:

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f"Vector: {self.args}"

    def __add__(self, other):
        a = []
        for i in range(len(self.args)):
            a.append(self.args[i] + other.args[i])
        return a

    def __sub__(self, other):
        s = []
        for i in range(len(self.args)):
            s.append((self.args[i] - other.args[i]))
        return s


    def length(self):
        len = 0
        for i in range(len(self.args)):
            l_vector += (self.args[i] * self.args[i])
        return round(math.sqrt(l_vector), 2)

    def scalar_Product(self, other):
        s_product = 0
        for i in range(len(self.args)):
            s_product += self.args[i] * other.args[i]
        return s_product

    def angle(self, other):
        a = self.scalar_Product(other)
        b = abs(self.len_vector()) * abs(other.len_vector())
        return round(a / b, 2)

    def cross_Product(self, other):

        x = self.__y * other.__z - self.__z * other.__y
        y = self.__z * other.__x - self.__x * other.__z
        z = self.__x * other.__y - self.__y * other.__x
        return Vector(x, y, z)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"Сложение векторов: {v1 + v2}")
    print(f"Вычитание векторов: {v1 - v2}")
    print(f"Длинна вектора: {v1.len_vector()}")
    print(f"Скалярное произведение векторов: {v1.scalar_Product(v2)}")
    print(f"Угол между вектарами: {v1.angle(v2)}")
