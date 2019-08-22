"""координаты вектора — это его проекции на соответствующие координатные оси"""


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

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


if __name__ == "__main__":
    v = Vector(1, 2, 3)
    print("X-axis projection: {}\nY-axis projection: {}\nZ-axis projection: {}".format(v.pr_x, v.pr_y, v.pr_z))

