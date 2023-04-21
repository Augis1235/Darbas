def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    return x / y

def keli_skaiciai(x, y):
    return x ** y

print("Galima!")
print("1.Sudėti")
print("2.Atimti")
print("3.Dauginti")
print("4.Dalinti")
print("5.Keliu skaičiu daugyba")

while True:
    pasirinkimas = input("Pasirinkite 1,2,3,4,5: ")

    if pasirinkimas in ("1", "2", "3", "4", "5"):
        try:
            pirmas_skaicius = float(input("Pirmas skaičius: "))
            antras_skaicius = float(input("Antras skaičius: "))
        except ValueError:
            print("Įvesta blogai!.")
            continue

        if pasirinkimas == "1":
            print(pirmas_skaicius, "+", antras_skaicius, "=", sudetis(pirmas_skaicius, antras_skaicius))

        elif pasirinkimas == "2":
            print(pirmas_skaicius, "-", antras_skaicius, "=", atimtis(pirmas_skaicius, antras_skaicius))

        elif pasirinkimas == "3":
            print(pirmas_skaicius, "*", antras_skaicius, "=", daugyba(pirmas_skaicius, antras_skaicius))

        elif pasirinkimas == "4":
            print(pirmas_skaicius, "/", antras_skaicius, "=", dalyba(pirmas_skaicius, antras_skaicius))

        elif pasirinkimas == "5":
            print(pirmas_skaicius, "**", antras_skaicius, "=", keli_skaiciai(pirmas_skaicius, antras_skaicius))

        ar_testi = input("Ar norite testi? TAIP/NE: ")
        if ar_testi == "NE":
            print("Viso gero, Gražios dienos!")
            break
    else:
        print("Blogai įvesta")
