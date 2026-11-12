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

class Sor:
    def __init__(self):
        self.adatok = []

    def betesz(self, adat):
        self.adatok.append(adat)

    def kivesz(self):
        if self.adatok:
            return self.adatok.pop(0)
        else:
            return None

    def ures(self):
        return len(self.adatok) == 0

    def meret(self):
        return len(self.adatok)

    def __str__(self):
        return "A sor adatai: " + " ".join(str(adat) for adat in self.adatok)

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

    print('*' * 40)

    s = Sor()      
    print(s)         
    print(s.ures())  
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         
    print(s.meret()) 
    print(s.ures())  
    x = s.kivesz()
    print(x)         
    print(s)         
    s.kivesz()
    s.kivesz()       
    x = s.kivesz()
    print(x)         

if __name__ == "__main__":
    main()