import math


class Vector:

    def __init__(self, *args):
       self.args = args

    def __add__(self, other):
        list_add = []
        for i in range(len(self.args)):
            list_add.append(self.args[i] + other.args[i])
        return list_add

    def __sub__(self, other):
        list_sub = []
        for i in range(len(self.args)):
            list_sub.append(self.args[i] - other.args[i])
        return list_sub

    @staticmethod
    def length(self):
        result_length = 0
        for i in range(len(self.args)):
            result_length += self.args[i] * self.args[i]
        return round(math.sqrt(result_length), 2)

    @staticmethod
    def scalar(first, second):
        result = 0
        for i in range(len(first.args)):
            result += first.args[i] * second.args[i]
        return result

    @classmethod
    def angle(cls, first, second):
        a = cls.scalar(first, second)
        b = abs(cls.length(first)) * abs(cls.length(second))
        return round(a / b, 2)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6, 9)
    print(f'Vector: {v1 + v2}')
    print(f'Vector: {v1 - v2}')
    print(f"Length vector: {Vector.length(v1)}")
    print(f"Scalar product of vectors: {Vector.scalar(v1, v2)}")

