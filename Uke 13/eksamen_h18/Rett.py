class Rett:

    def __init__(navn, pris, innholdsstoffer):
        self._navn = navn
        self._pris = pris
        self._innholdsstoffer = innholdsstoffer

    def sjekkInnholdOK(self, innholdsstoffer):
        for stoff in innholdsstoffer:
            if stoff in self._innholdsstoffer:
                return False
        return True

    def __str__(self):
        rett = self._navn + ": " + str(self._pris)
        innhold = "Innhold: "
        for i in self_innholdsstoffer:
            innhold += (i + ", ")
        innhold = innhold[:-2]
        return rett + innhold


