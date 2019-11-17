class Kunde:

    def __init__(self, tlf, innholdsstoffer):
        self._tlf = tlf
        self._innholdsstoffer = innholdsstoffer

    def velgRetter(self, meny):
        redusertMeny = meny.hentRedusertMeny(self._innholdsstoffer)
        bestilling = []
        # Mangler hentemetoder, skriver ut hele kategorien
        for kat in redusertMeny.values():
            print(kat)
            print(redusertMeny[kat])
            rett = input("Oppgi rett")
            if rett != "":
                bestilling.append(rett)
        return bestilling
