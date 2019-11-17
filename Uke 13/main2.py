"""
Dette er et alternativt hovedprogram som man kan kjøre med sitt eget Game of Life-program.
Det gjør at man kan laste ned mønstre fra nettet og kjøre dem, f.eks. "guns" som lager interessante figurer.
Legg denne filen main2.py i din egen Game of Life-mappe, og kjør den i stedet for det vanlige hovedprogrammet.
Last ned filer fra nettet, eller fra 'patterns'-mappen her på GitHub.
Skriv inn filnavnet i programmet for å laste inn et mønster.
Flere patterns kan finnes her: https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life#patterns
Fungerer kun med filer som slutter på .cells.
"""

import time
from spillebrett import Spillebrett

def main():
    filnavn = input("Oppgi filnavn: ")
    minRad, minKol = dimensjonerFraFil(filnavn)
    print("Minimum størrelse på spillebrettet er: " + str(minKol) + " × " + str(minRad) + ".") 
    antKol = int(input("Oppgi antall kolonner: "))
    antRad = int(input("Oppgi antall rader: "))
    spillebrett = lesFraFil(filnavn, antRad, antKol)
    spillebrett.tegnBrett()
    kommando = input("Skriv 'auto' for automatisk oppdatering eller trykk <Enter> for manuell oppdatering: ").lower()
    while kommando == "":
        if kommando != "q":
            spillebrett.oppdatering()
            print("\033[2J")
            spillebrett.tegnBrett()
            print("Generasjon:", spillebrett.generasjonsnummer, "- Antall levende celler:", spillebrett.finnAntallLevende())
        kommando = input("Trykk <Enter> for neste generasjon. <q> for å avslutte: ").lower()
    while kommando == "auto":
        time.sleep(0.05)
        spillebrett.oppdatering()
        print("\033[2J")
        spillebrett.tegnBrett()
        print("Generasjon:", spillebrett.generasjonsnummer, "- Antall levende celler:", spillebrett.finnAntallLevende())

def dimensjonerFraFil(filnavn):
    antRad = 0
    antKol = 0
    with open(filnavn) as fil:
        for linje in fil:
            if linje[0] != "!":
                antRad += 1
                antKol = max(len(linje), antKol)
    return antRad, antKol

def lesFraFil(filnavn, antRad, antKol):
    spillebrett = Spillebrett(antRad, antKol)
    for rad in spillebrett._matrise:
        for celle in rad:
            celle.settDoed()
    spillebrett.tegnBrett()
    with open(filnavn) as fil:
        curRad = -1
        for linje in fil:
            if linje[0] != "!":
                curRad += 1
                for curKol in range(len(linje)):
                    if linje[curKol] == "O":
                        spillebrett._matrise[curRad][curKol].settLevende()
    return spillebrett

main()
