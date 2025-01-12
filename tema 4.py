import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Cuvântul de ghicit: " + " ".join(progres))
print(f"Număr de încercări rămase: {incercari_ramase}\n")

while incercari_ramase > 0 and "_" in progres:

    litera = input("Introdu o literă: ").lower()


    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o literă validă.")
        continue


    if litera in litere_incercate:
        print(f"Litera '{litera}' a fost deja încercată. Încearcă alta.")
        continue


    litere_incercate.append(litera)


    if litera in cuvant_de_ghicit:

        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print(f"Corect! {litera} este în cuvânt!")
    else:

        incercari_ramase -= 1
        print(f"Greșit! {litera} nu este în cuvânt.")


    print("Cuvântul de ghicit: " + " ".join(progres))
    print(f"Număr de încercări rămase: {incercari_ramase}\n")


if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul!")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
