print("Zadanie1")
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(tekst)
print("Zadanie2")
imie = "Mateusz"
nazwisko = "Białek"
litera_1 = imie[2]
litera_2 = nazwisko[3]
tekst2 = "W tekście jest liter ... oraz liter ..."
liczba_liter1 = tekst2.count(litera_1)
liczba_liter2 = tekst2.count(litera_2)
print('W tekście jest {0} liter {1} oraz {2} liter {3}'.format(liczba_liter1, litera_1, liczba_liter2, litera_2))
print("zadanie5")
tekst3 = "Mateusz Białek"
print(tekst3[::-1])
print("Zadanie6")
lista = [1,2,3,4,5,6,7,8,9,10]
print("Lista: ", lista)
lista2 = []
lista2.append(lista[5])
for i in range(6, 10):
    lista2.append(lista[i])

for i in range(6, 11):
    lista.remove(i)


print("Lista2:  ",lista2)
print("Lista1:  ", lista)

print("Zadanie7")
lista.extend(lista2)
print("Lista: ", lista)

print("Zadanie8")
krotka = (153732, "Jan Kowalski", 253757, "Pawel Nowak")
print(krotka)

print("Zadanie9")
slownik = dict([("nr_indeksu", 153732), ("imie_nazwisko", "Jan Kowalski")])
slownik["data_ur"] = "15.09.1998"
slownik["wiek"] = 22
slownik["adres"] = "Sloneczna 5/7"
print("Slownik: ", slownik)

print("Zadanie10")
lista_numery = [997,998,999,998,112, 112, 112]
lista_numery = set(lista_numery)
print("Lista z numerami: ", lista_numery)

print("Zadanie11")
for i in range(1, 11):
    print(i)

print("Zadanie12")
for i in range(100, -21, -5):
    print(i)

print("Zadanie13")
slownik2 = dict([("numer", 123456789), ("imie", "Jan")])
lista_slownik = [1,2,5,slownik2, "Kot"]
napis = str(lista_slownik)
print(napis)
