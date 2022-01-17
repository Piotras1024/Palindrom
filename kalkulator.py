import logging
logging.basicConfig(level=logging.DEBUG)


def dodawanie(zbiorliczb):
    suma = 0
    for liczba in zbiorliczb:
        suma = suma + liczba
    return(suma)
def mnozenie(zbiorliczb):
    suma = 1
    for liczba in zbiorliczb:
        suma = suma * liczba
    return (suma)
def odejmowanie(zbiorliczb):
    suma = zbiorliczb[0] - zbiorliczb[1]
    return (suma)
def dzielenie(zbiorliczb):
    suma = zbiorliczb[0] / zbiorliczb[1]
    return(suma)

print("Podaj działanie, posługując się odpowiednią liczbą: 1 dodawanie, 2 mnożenie, 3 dzielenie, 4 odejmowanie:")
odp = int(input())
pierwszaliczba = int(input("Podaj składnik 1.: "))
drugaliczba = int(input("Podaj składnik 2: "))
zbiorliczb = [pierwszaliczba, drugaliczba]
if odp == 1:
    wynik_dodawania = dodawanie(zbiorliczb)
    logging.debug("Dodaję %s i %s" % (zbiorliczb[0], zbiorliczb[1]))
    logging.debug("Wynik to %s" % (wynik_dodawania))
if odp == 2:
    wynik_mnozenia = mnozenie(zbiorliczb)
    logging.debug("Mnożę %s i %s" % (zbiorliczb[0], zbiorliczb[1]))
    logging.debug("Wynik to %s" % (wynik_mnozenia))


if odp == 3:
    wynik_dzielenia = dzielenie(zbiorliczb)
    logging.debug("Dziele %s i %s" % (zbiorliczb[0], zbiorliczb[1]))
    logging.debug("Wynik to %s" % (wynik_dzielenia))
if odp == 4:
    wynik_odejmowania = odejmowanie(zbiorliczb)
    logging.debug("Odejmuje %s i %s" % (zbiorliczb[0], zbiorliczb[1]))
    logging.debug("Wynik to %s" % (wynik_odejmowania))
