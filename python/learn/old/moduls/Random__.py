import random

print(random.randint(1, 8))     # zufällige ganze Zahl von 1 bis 8

value = random.random()         # zufälliege Zahl von 0 bis 0.999...
print(value)

value = random.uniform(1, 10)   # zufällige Zahl ZWISCHEN 1 und 10
print(value)

Sandwiches = ["Backfisch", "Sushi", "Unigiri", "Date a live", "death note", "Darling in the Franxx"]
value = random.choice(Sandwiches) # wählt zufällig aus Listen :b
print(value)

Backfische = random.choices(Sandwiches, k=3)   # wählt drei zufälliege Sachen aus "Sandwiches" aus
print(Backfische)

Backfische = random.choices(Sandwiches, weights=[5, 5, 1, 3, 1, 1], k=3)   # fügt Wahrscheinlichkeiten dazu
print(Backfische)

buch = list(range(1, 53))
random.shuffle(buch)              # mischt "buch"
print(buch)

deck = list(range(1, 53))
hand = random.sample(deck, k=5)   # mischt "deck" und had 5 Karten als output (functioniert NICHT mit "shuffle")
print(hand)                       # nichts wiederholt sich


Sandwiches = ["Backfisch", "Sushi", "Unigiri", "Date a live", "death note", "Darling in the Franxx"]
value = random.choice(Sandwiches) # wählt zufällig aus Listen :b
print(value)