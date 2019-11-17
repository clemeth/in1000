class Meny:

    def __init__(self, kategorinavn):
        self._meny = {}

        for navn in kategorinavn:
            filnavn = navn + ".txt"
            self._meny[navn] = self._lesKategoriFil(filnavn)

    def hentRedusertMeny(self, innholdsstoffer):
        redusertMeny = {}

        for kategori in self._meny:
            okRetter = self._meny[kategori].hentOkRetter(innholdsstoffer)
            if okRetter is not []: 
                okKategori = Kategori(kategori, okRetter)
                redusertMeny[kategori] = okKategori

        return redusertMeny






