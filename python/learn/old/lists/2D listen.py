
number_grid = [
    [1, 2, 3],                   # hier ist eine Liste in einer Liste
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])        # druckt Zeile 1, Spalte 2

print()

for row in number_grid:         # druckt villeicht jede Zeile von "number_grid"
    print(row)

    print()

for row in number_grid:         # druckt alle Daten aus "number_grid" und außerdem hab ich echt hunger
    for col in row:
        print(col)


