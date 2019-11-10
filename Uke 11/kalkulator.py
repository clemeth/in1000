class Kalkulator:

    def kalkuler(self, regnestykke):
        regnestykke = regnestykke.split()
        tall1 = int(regnestykke[0])
        tegn = regnestykke[1]
        tall2 = int(regnestykke[2])
        if tegn == "+":
            return self.adder(tall1, tall2)
        if tegn == "-":
            return self.subtraher(tall1, tall2)
        if tegn == "/":
            if tall2 != 0:
                return self.divider(tall1, tall2)
            else:
                return "Nulldivisjon"
        if tegn == "*":
            return self.multipliser(tall1, tall2)
        if tegn == "^":
            return self.eksponer(tall1, tall2)

    def adder(self, tall1, tall2):
        return tall1 + tall2

    def subtraher(self, tall1, tall2):
        return tall1 - tall2

    def divider(self, tall1, tall2):
        return tall1 / tall2

    def multipliser(self, tall1, tall2):
        return tall1 * tall2

    def eksponer(self, tall1, tall2):
        return tall1 ** tall2
