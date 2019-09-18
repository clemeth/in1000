liste = []

for i in range(5):
    tall = int(input("Skriv inn tall " + str(i+1) + ": "))
    liste.append(tall)

def storste(enListe):
    storsteTall = enListe[0]
    for tall in enListe:
        if tall > storsteTall:
            storsteTall = tall
    return storsteTall

print(storste(liste))
print(liste)
