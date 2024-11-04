meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = {"papanasi": 7, "ceafa": 10, "guias": 5}
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

incasari = []

for student in studenti:
    if not comenzi or not tavi:
        break
    comanda = comenzi.pop(0)
    tavă = tavi.pop()
    istoric_comenzi.append(comanda)
    incasari.append(preturi[comanda])

    print(f"{student} a comandat {comanda}.")

suma_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}

for comanda in istoric_comenzi:
    suma_comenzi[comanda] += 1

print(f"S-au comandat {suma_comenzi['guias']} guias, {suma_comenzi['ceafa']} ceafa, {suma_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {suma_comenzi['ceafa'] < 3}.")
print(f"Mai sunt papanasi: {suma_comenzi['papanasi'] < 10}.")
print(f"Mai sunt guias: {suma_comenzi['guias'] < 6}.")

total_venit = sum(incasari)
print(f"Cantina a încasat: {total_venit} lei.")

produse_mici = [produs for produs in preturi.items() if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_mici}.")