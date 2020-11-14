import file_manager

print("Wczytanie pliku przed aktualizacja")
objekt = file_manager.FileManager("plik")
print(objekt.read_file())

print("Wczytanie pliku po aktualizacji")
objekt.update_file("Nowy tekst")
print(objekt.read_file())