import random

def odaberi_rijec():
    rijeci = ["povijest", "muzej", "pozega", "umjetnost", "slikarica", "marija"]
    return random.choice(rijeci)

def igraj():
    rijec = odaberi_rijec()
    pogodi_rijec = "_" * len(rijec)
    broj_pokusaja = 7
    vec_pogodene = []

    print("Dobrodošli u igru Pogodi Riječ!")
    print("Riječ ima", len(rijec), "slova.")

    while broj_pokusaja > 0 and "_" in pogodi_rijec:
        print("Riječ:", " ".join(pogodi_rijec))
        print("Pogodite slovo (preostalo pokušaja:", broj_pokusaja, "):")
        unos = input().lower()

        if len(unos) != 1 or not unos.isalpha():
            print("Unesite samo jedno slovo.")
            continue

        if unos in vec_pogodene:
            print("Već ste pogađali to slovo.")
            continue

        if unos in rijec:
            for i in range(len(rijec)):
                if rijec[i] == unos:
                    pogodi_rijec = pogodi_rijec[:i] + unos + pogodi_rijec[i+1:]
        else:
            broj_pokusaja -= 1

        vec_pogodene.append(unos)

    if "_" not in pogodi_rijec:
        print("Čestitamo, pogodili ste riječ:", rijec)
    else:
        print("Izgubili ste. Riječ je bila:", rijec)

if __name__ == "__main__":
    igraj()
