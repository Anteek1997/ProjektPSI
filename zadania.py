# Zadanie1
tekst =      "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po " \
             "raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. /," \
             "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
             "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
             "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do " \
             "realizacji druków na komputerach osobistych, jak Aldus PageMaker "
# Zadanie2
imie = "Bartosz"
nazwisko = "Antkiewicz"
liczba_liter1 = tekst.lower().count(imie[1])
liczba_liter2 = tekst.lower().count(nazwisko[2])
print(f'W tekście jest {liczba_liter1} {imie[1]} oraz {liczba_liter2} {nazwisko[2]}')

# Zadanie3 w nowym pliku formatowanieCiagow.py
# Zadanie4
# print(dir(loremIpsum))
# help(loremIpsum.istitle())

# Zadanie5
extendedSlice = imie.lower()[::-1].capitalize() + '' + nazwisko.lower()[::-1].capitalize()
print(extendedSlice)

# Zadanie6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:10]
lista = lista[0:5]
print(lista)
print(lista2)

# Zadanie7
lista3 = lista + lista2
lista3.insert(0, 0)
print(lista3)
lista4 = lista3.copy()
lista4.sort(reverse=True)
print(lista3)
print(lista4)

# Zadanie8
student1 = (111111, "Piotr Nowak")
student2 = (122222, "Bartosz Antkieiwcz")
student3 = (133333, "Tomasz Abacki")
student4 = (144444, "Piotr Kowalksi")
student5 = (155555, "Mateusz Białek")
student6 = (166666, "Piotr Piotr")
student7 = (17777, "Cezary Cezary")

listaStudentow = [student1, student2, student3, student4, student5, student6, student7]
print(listaStudentow)

# Zadanie 9
slownik = dict([student1, student2, student3, student4, student5, student6, student7])
print(slownik)

slownik[111111] = [slownik.get(111111), 22, "123@wp.pl", 1998, "Podmiejska 1"]
slownik[122222] = [slownik.get(122222), 21, "bartek@wp.pl", 1999, "Podmiejska 2"]
slownik[133333] = [slownik.get(133333), 20, "12323@wp.pl", 1998, "Podmiejska 3"]
print(slownik)

# Zadanie 10

listaKontaktow = [12345, 12345, 12346, 11111]
listaUnikalnych = list(set(listaKontaktow))
print(listaUnikalnych)

# Zadanie 11

for i in range(1, 11):
    print(i)

# Zadanie 12
for j in range(100, 19, -5):
    print(j)

# Zadanie 13
lista = [
    {"Imie": "Jan", "Nazwisko": "Bernard", "Wiek": 65, "Numer": 111111111},
    {"Imie": "Jarosław", "Nazwisko": "Cichociemny", "Wiek": 35, "Numer": 222222222},
    {"Imie": "Michał", "Nazwisko": "Adamek", "Wiek": 86, "Numer": 333333333}
]
for x in lista:
    print(f"Imie i nazwisko: {x['Imie']} {x['Nazwisko']}, wiek: {x['Wiek']}, numer telefonu: {x['Numer']}")
