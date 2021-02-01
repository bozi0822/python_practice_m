class Point:

    __private = 1
    public = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def __del__(self):
        class_name = self.__class__.__name__
        print("%s is destroyed" % class_name)


if __name__ == '__main__':
    point = Point(3, 4)
    print(point)
    print(point.public)
    print(point.get_x())
    point.set_x(10)
    print("=====================")

    print(point.get_x())
