import random

print("Dobrodošli u pogodi broj")
print("Mislim na broj između 1 i 100.")
print("imate 7 pokušaja.")

broj = random.randint(1, 100)
pokušaja = 0

while pokušaja < 7:
    guess = int(input("Pogodi broj: "))
    pokušaja += 1

    if guess < broj:
        print("broj je premali.")
    elif guess > broj:
        print("broj je prevelik.")
    else:
        print(f"Čestitamo! pogodili ste broj u {pokušaja} pokušaja.")
        break

if pokušaja == 7:
    print(f"Nažalost, ostali ste bez pokušaja. broj je {broj}.")
