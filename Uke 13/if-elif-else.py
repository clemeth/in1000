# Det er viktig å bruke elif riktig, her er et eksempel der vi sjekker om et tall er 15, 13 eller ingen av delene.

x = 15

if x == 15:
    print("Tallet er 15")
# Her burde det stått elif. Prøvekjør programmet, så ser man problemet :)
if x == 13:
    print("Tallet er 13")
else:
    print("Ingen av delene")
