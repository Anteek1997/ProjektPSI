print("Zadanie1")
def dodaj(a_list, b_list):
    lista = []
    for i in range(0, len(a_list)):
        if i / 2 == 0:
            lista.append(a_list[i])
        else:
            lista.append(b_list[i])
    return lista

a_list = [5,4,3,4,5,6,7,8,9]
b_list = [2,5,3,4,5,6,7,8,9]

print(dodaj(a_list, b_list))

print("Zadanie2")
def funkcja(data_text):
    slownik = {}
    slownik["dlugosc"] = len(data_text)
    return slownik


