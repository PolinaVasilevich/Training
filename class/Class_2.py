"""координаты вектора — это его проекции на соответствующие координатные оси"""


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def pr_x(self):
        return self.x

    @property
    def pr_y(self):
        return self.y

    @property
    def pr_z(self):
        return self.z

    @pr_x.setter
    def pr_x(self, x):
        self.x = x

    @pr_y.setter
    def pr_y(self, y):
        self.y = y

    @pr_z.setter
    def pr_z(self, z):
        self.z = z


if __name__ == "__main__":
    v = Vector(1, 2, 3)
    print("X-axis projection: {}\nY-axis projection: {}\nZ-axis projection: {}".format(v.pr_x, v.pr_y, v.pr_z))
