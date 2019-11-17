# Det er flere måter å gå gjennom filer. 

# Med for-loop

fil = open('fil.txt')

for linje in fil:
    print(linje)

# Med while-løkke

linje = fil.readline()

while linje != "":
    print(linje)
    linje = fil.readline()

# Hvis man kjører dette programmet vil man se at filen bare skrives ut én gang fram til nå.
print('Bare én gang fram til nå.')
# Dette er fordi filer blir "brukt opp", og man må enten åpne dem på nytt eller bruke metoden seek() for å gå tilbake til start i filen.

fil.seek(0) # går tilbake til start

linje = fil.readline()
while linje != '': # mens linjen ikke er tom (altså siste linje som regel)
    print(linje)
    linje = fil.readline()

# Nå kom den en gang til. Eventuelt kan man bare skrive:

fil.close()
fil = open('fil.txt')

for linje in fil:
    print(linje)
