tekst = "Programowanie Serwisów Internetowych"
print('{:^50}'.format(tekst))
print('{:>50}'.format(tekst))
liczba = 3.141592653589793
print('{:06.2f}'.format(liczba))
print('{:.13}'.format(tekst))
person = {'first': 'Jan', 'last': 'Kowalski'}
print('{p[first]} {p[last]}'.format(p=person))

print(dir(tekst))
help(tekst.center)