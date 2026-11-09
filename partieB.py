def generate(genome, position):
    # Cas de base : la séquence est terminée
    if position == len(genome):
        for i in range(len(genome)):
            print(genome[i], end="")
        print()
        return

    # Cas récursif : insérer les quatre valeurs possibles : 0, 1, 2 et 3
    for i in range(1,4):
        genome[position] = i
        generate(genome, position + 1)


n = 5
genome = [0] * n
generate(genome, 0)

"""
partie B --> générer toutes les séquences pour n dans l'alphabet {c, g, t} soit {2, 3, 4}, sans le a.
"""