class Verem:
    def __init__(self):
        self.adatok = []

    def betesz(self, adat):
        self.adatok.append(adat)

    def kivesz(self):
        if self.adatok:
            return self.adatok.pop()
        else:
            return None

    def ures(self):
        return len(self.adatok) == 0

    def meret(self):
        return len(self.adatok)

    def __str__(self):
        return "A verem adatai: " + " ".join(str(adat) for adat in self.adatok)

class MyQueue:
    def __init__(self):
        self.bemenet = Verem()
        self.kimenet = Verem()
 
    def append(self, elem):
        self.bemenet.betesz(elem)
 
    def popleft(self):
        if self.is_empty():
            print("Üres sorból nem lehet elemet kivenni")
        if self.kimenet.ures():
            while not self.bemenet.ures():
                self.kimenet.betesz(self.bemenet.kivesz())
        return self.kimenet.kivesz()
 
    def is_empty(self):
        return self.bemenet.ures() and self.kimenet.ures()
 
    def size(self):
        return self.bemenet.meret() + self.kimenet.meret()


def main():
    q = MyQueue()
    print(q.is_empty())  # True
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.size())      # 3
    print(q.popleft())   # 1
    print(q.popleft())   # 2
    print(q.size())      # 1
    print(q.is_empty())  # False
    print(q.popleft())   # 3
    print(q.is_empty())  # True

if __name__ == "__main__":
    main()