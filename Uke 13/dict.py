ordbok = {}

ordbok[5] = 21
ordbok[6] = 55
ordbok[1] = 36
ordbok[10] = 24

# Finne største nøkkelverdi
bigKey = 0

for key in ordbok.keys():
    if key > bigKey:
        bigKey = key

print(bigKey)

# Finne største innholdsverdi
bigVal = 0

for val in ordbok.values():
    if val > bigVal:
        bigVal = val

# For å skrive ut nøkkelverdien som har størst innholdsverdi må vi iterere gjennom til vi finner en match.
for i in ordbok:
    if ordbok[i] == bigVal:
        print(i)

print(bigVal)
