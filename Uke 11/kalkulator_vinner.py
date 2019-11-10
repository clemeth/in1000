class Kalkulator:

    def kalkuler(self, streng):
        liste = streng.split()
        tall1 = int(liste[0])
        tegn = liste[1]
        tall2 = int(liste[2])
        if tegn == "+":
            return self.adder(tall1, tall2)
        if tegn == "-":
            return self.subtraher(tall1, tall2)
        if tegn == "/":
            return self.divider(tall1, tall2)
        if tegn == "^":
            return self.eksponer(tall1, tall2)
        if tegn == "*":
            return self.multipliser(tall1, tall2)


    def adder (self, tall1, tall2):
        return tall1 + tall2

    def subtraher (self, tall1, tall2):
        return tall1 - tall2

    def divider (self, tall1, tall2):
        if tall2 == 0:
            return "Nulldivisjon "
        return tall1 / tall2

    def eksponer(self, tall1, tall2):
        return tall1 ** tall2

    def multipliser(self, tall1, tall2):
        return tall1 * tall2
