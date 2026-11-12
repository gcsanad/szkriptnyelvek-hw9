class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * 3.14 * (self.radius ** 3)

    def area(self):
        return 4 * 3.14 * (self.radius ** 2)

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return 3.14 * self.a * self.b

def main():
    sphere = Sphere(5)
    ellipse = Ellipse(3, 4)

    print("Gömb térfogata:", sphere.volume())
    print("Gömb felülete:", sphere.area())
    print("Ellipsz felülete:", ellipse.area())

if __name__ == "__main__":
    main()