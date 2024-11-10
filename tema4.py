import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la Spânzurătoare!")
print("Cuvântul de ghicit este:", " ".join(progres))
print("Ai la dispoziție 6 încercări.")

while "_" in progres and incercari_ramase > 0:

    print(f"Progres: {' '.join(progres)}")
    print(f"Încercări rămase: {incercari_ramase}")
    print("Litere încercate:", ", ".join(litere_incercate))

    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue

    if litera in litere_incercate:
        print(f"Ai încercat deja litera '{litera}'. Te rog să alegi altă literă.")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:

        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print(f"Litera '{litera}' se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print(f" Litera '{litera}' nu se află în cuvânt.")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
