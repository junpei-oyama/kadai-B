class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        s = self.height * self.width
        return print('{0:.2f}'.format(s))

    def diagonal(self):
        d = (self.height ** 2 + self.width ** 2) ** 0.5
        return print('{0:.2f}'.format(d))


def main():
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()
    rectangle1.diagonal()

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()
    rectangle2.diagonal()


if __name__ == '__main__':
    main()
