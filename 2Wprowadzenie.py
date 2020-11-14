print("Zadanie1")


def dodaj(a_list, b_list):
    lista = []
    for i in range(0, len(a_list)):
        if i / 2 == 0:
            lista.append(a_list[i])
        else:
            lista.append(b_list[i])
    return lista


a_list = [5, 4, 3, 4, 5, 6, 7, 8, 9]
b_list = [2, 5, 3, 4, 5, 6, 7, 8, 9]

print(dodaj(a_list, b_list))

print("Zadanie2")


def funkcja2(data_text):
    slownik = {}
    slownik["dlugosc"] = len(data_text)
    slownik["litery"] = [char for char in data_text]
    slownik["duze litery"] = data_text.upper()
    slownik["male litery"] = data_text.lower()
    return slownik


print(funkcja2("Projektowanie systemów informatycznych"))

print("Zadanie3")


def funkcja3(tekst, litera):
    tekst2 = tekst.replace(litera, '')
    return tekst2


print(funkcja3("zadania", "a"))

print("Zadanie4")


def przelicz(temperatura, temperature_type):
    if temperature_type == "F":
        stopnie = temperatura * 1.8 + 32
    elif temperature_type == 'K':
        stopnie = temperatura + 273.15
    elif temperature_type == 'R':
        stopnie = 1.8 * (temperatura + 273.15)
    return stopnie

print("30 stopni Celcjusza to: ", przelicz(30, "F"), " stopni Fahrenheita")
print("30 stopni Celcjusza to: ", przelicz(30, "K"), " stopni Kelwina")
print("30 stopni Celcjusza to: ", przelicz(30, "R"), " stopni Rankina")

print("Zadnaie5")
class Calculator:
    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def podziel(self, a, b):
        return a / b

    def pomnoz(self, a, b):
        return a * b

obiekt = Calculator()
print("Dodawanie:", obiekt.dodaj(10,5))
print("Odejmowanie:", obiekt.odejmij(10,5))
print("Dzielenie:", obiekt.podziel(10,5))
print("Mnożenie:", obiekt.pomnoz(10,5))

print("Zadanie6")
class ScienceCalculator(Calculator):
    def poteguj(self, a, b):
        return a**b

obiekt2 = ScienceCalculator()
print("Potegowanie:", obiekt2.poteguj(10,5))

print("Zadanie7")
def odwrtnie(tekst):
    return tekst[::-1]

zmienna = "tekst"
print(odwrtnie(zmienna))