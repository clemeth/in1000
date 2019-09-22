ordbok = {"hei":1,
        "hadet":2}

print(ordbok)

# Det kan ikke være like nøkkelverdier. Et tilegning av innholdsverdi på en nøkkelverdi som allerede finnes vil endre den
ordbok["hei"] = 3

print(ordbok)

# Nye nøkkelverdier kan legges til på samme måte
ordbok["test"] = 5

print(ordbok)

# Man skriver ut innholdsverdien til nøkkelverdiene ved å kalle på nøkkelverdiene
print(ordbok["hei"])
