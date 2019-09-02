# Uke 2

Stikkord: [input](input.py), [feilmeldinger](feilmeldinger.py), [evaluering](evaluering.py), [typekonvertering](typekonvertering.py), [prosedyrer](prosedyrer.py).

## Et par kommentarer fra forrige uke

* Bruk riktig Python-versjon (Python 3)!
* [Trix](https://trix.ifi.uio.no)

## Tilkoblig til ifi-maskiner

### SSH og SCP

For å laste opp eller ned filer til ifi-maskinene kan du bruke kommandoen *scp*, f.eks. slik:

```
  scp /mappe/fil.py brukernavn@login.uio.no:~/Documents/
```

Dette vil laste opp en fil som heter "fil.py" som ligger i mappen "mappe" til "Documents"-mappa på ifi-maskinen. Hvis man så vil kjøre denne kan man bruke *ssh* som nedenfor, og kjøre programmet ved å skrive `python3 /Documents/fil.py`. For å laste noe ned fra ifi-maskinene bare bytter du om på rekkefølgen, f.eks. som dette:

```
  scp brukernavn@login.uio.no:~/Documents/fil.py /mappe/
```

For å fjernstyre en ifi-maskin kan du bruke kommandoen *ssh* i terminalen. Dette kan gjøres ved å skrive inn følgende og trykke enter (bytt ut *brukernavn* med ditt eget brukernavn):

```
  ssh brukernavn@login.uio.no
```

Du vil så bli bedt om å skrive inn passord. Når du har gjort det og trykket enter er terminalen din da logget inn på en ifi-maskin, hvor du kan bruke terminalkommander som vanlig.

### Cyberduck

Et annet alternativ er å bruke [Cyberduck](https://www.uio.no/tjenester/it/lagring-samarbeid/hjemmeomrader/hjemmeomrade/mac/).
