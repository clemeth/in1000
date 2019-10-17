class Sannhet:

    def __init__(self, sant):
        self._sant = sant

    def erSann(self):
        return self._sant

sannhet1 = Sannhet(True)
sannhet2 = Sannhet(False)

if sannhet1.erSann():
    print("Sannhet 1 er sann")
