import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi

    def area(self):
        s = self.radius ** 2 * self.pi
        return round(s, 2)

    def perimeter(self):
        circ_len = self.radius * 2 * self.pi
        return round(circ_len, 2)


def main():
    # 半径1の円
    circle1 = Circle(radius=1)
    print(circle1.area())
    print(circle1.perimeter())

    circle3 = Circle(radius=3)
    print(circle3.area())
    print(circle3.perimeter())


if __name__ == '__main__':
    main()
