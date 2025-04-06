"""
siema
"""


class Ksiazka:
    """
    klasa ksiazki
    """
    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = (tytul,)
        self.autor = (autor,)
        self.dostepna = dostepna


class Biblioteka:
    """
    klasa biblioteka
    """
    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """
        dodaj_ksiazke
        """
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """
        wypozycz ksiazke
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul and ksiazka.dostepna:
                ksiazka.dostepna = False
                return f"Wypozyczono: {tytul}"
            return f"Ksiazka {tytul} niedostepna"

    def zwroc_ksiazke(self, tytul):
        """
        zwroc_ksiazke
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """
        dostepne_ksiazki
        """
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.Tytul)
        return dostepne


def main():
    """
    main
    """
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
