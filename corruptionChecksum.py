def main():
    vegsoOsszeg = 0
    with open("dataAdvent.txt", "r", encoding="utf-8") as fajl:
        for sor in fajl:
            szamok = sor.split('\t')
            maxMinKulonbseg = max(int(szam) for szam in szamok) - min(int(szam) for szam in szamok)
            vegsoOsszeg += maxMinKulonbseg
    print("A végső összeg:", vegsoOsszeg)


if __name__ == "__main__":
    main()