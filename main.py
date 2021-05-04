name_magicians = ["Sumir a carta", "Adivinhando o numero", "sumir a moeda"]

magicos = ['Humberto', 'Wesley', 'Fabricio']


def make_great():
    for nm in name_magicians:
        for mgc in magicos:
            print('O Grande ' + mgc + ' fez o truque de ' + nm)

magica = magicos.copy()

print(make_great())

def magic():
    for m in magica:
        for mn in name_magicians:
            print("O Grande Magico " + m + "Fez o truque de " + name_magicians)