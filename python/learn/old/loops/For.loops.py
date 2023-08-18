
for letter in "Giraffe Academy":                  # druckt jedes Zeichen in "Giraffe Academy"
    print(letter)

friends = ["Jimmy", "Kevin", "Hans"]

for friend in friends:                            # druckt alle Daten aus "friends"
    print(friend)

for index in range(3, 10):                        # Bereich von 3-10 (10 wird nicht gedruckt)
    print(index)

for index in range(len(friends)):                 # druckt hoffentlich auch alle Daten aus "friends" nur in kompliziert
    print(friends[index])

for index in range(5):                            # druckt ein mahl "Erster Durchgang" und sonst was anderes
    if index == 0:
        print("Erster durchgang")
    else:
        print("Nicht erster Durchgang")