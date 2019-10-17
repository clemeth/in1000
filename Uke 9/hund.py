from random import randint

class Hund:

    def __init__(self, kjonn, navn, alder):
        self._kjonn = kjonn # 1 = gutt, 0 = jente
        self._navn = navn
        self._alder = alder

    def __str__(self):
        if self._kjonn == 0:
            kjonn = "jente"
        else:
            kjonn = "gutt"
        streng = self._navn + " er en " + kjonn + " og er " + str(self._alder) + " år gammel"
        return streng

    def __eq__(self, hund):
        # Hunder er like om de er samme kjønn
        return self._kjonn == hund.hentKjonn()

    def hentKjonn(self):
        return self._kjonn

    def hentNavn(self):
        return self._navn

class Kennel:

    def __init__(self, rad, kol):
        self._rader = rad
        self._kolonner  = kol
        self._hundeliste = self.generer(rad, kol) 

    def generer(self, rader, kolonner):
        navneliste = ["Abe", "Ace", "Achilles", "Zeus", "Agar", "Aiden", "Ajax", "Amigo", "August", "Artemis", "Hades"]
        max_alder = 15
        hundeliste = []
        for r in range(rader):
            hundeliste.append([])
            for k in range(kolonner):
                kjonn = randint(0,1)

                navn_indeks = randint(0, len(navneliste)-1)
                navn = navneliste[navn_indeks]

                alder = randint(0, max_alder)

                hund = Hund(kjonn, navn, alder)

                hundeliste[r].append(hund)

        return hundeliste

    def hentHund(self, rad, kol):
        return self._hundeliste[rad][kol]

    def skrivHunder(self):
        for r in range(self._rader):
            tekst = "Rad " + str(r) + " har hundene: "
            for k in range(self._kolonner):
                tekst += self.hentHund(r, k).hentNavn() + ", "
            print(tekst)

# Her slutter klassen og hovedprogrammet fortsetter

def hovedprogram():

    kennel = Kennel(4, 4)
    kennel.skrivHunder()

    if kennel.hentHund(0,0) == kennel.hentHund(0,1):
        print("Nabohundene på 0,0 og 0,1 er samme kjønn")

    print(kennel.hentHund(0,0))

hovedprogram()
