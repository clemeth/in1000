class Kategori:

    def __init__(self, navn, retter):
        self._kategorinavn = navn
        self._retter = retter

    def hentOkRetter(self, innholdsstoffer):
        okRetter = []
        for rett in self._retter:
            if rett.sjekkInnholdOK(innholdsstoffer):
                okRetter.append(rett)
        return okRetter
