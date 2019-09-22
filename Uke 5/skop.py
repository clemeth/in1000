variabel = 10

# Gir UnboundLocalError, siden variabel ikke er i skopet til prosedyren
def leggTilTi():
    variabel += 10

# Bruker try-except for å fange erroren og tillate programmet å fortsette å kjøre
try:
    leggTilTi()
except UnboundLocalError:
    print("Oops")

# Prosedyrer har med andre ord tilgang på å bruke variabler, men ikke endre dem
def printVariabel():
    print(variabel)

def leggTilTiTilNy():
    nyvariabel = variabel + 10
    print(nyvariabel)

leggTilTiTilNy()

printVariabel()

print(variabel)

# Hvis vi bruker parametre og returverdier kan vi få tilgang på alt som blir sendt inn, parametre er en måte å gi prosedyrer/funksjoner tilgang!
def leggTilTi(variabel):
    variabel += 10
    return variabel

print(leggTilTi(variabel))

# Men selve variabelen har ikke blitt endret
print(variabel)
