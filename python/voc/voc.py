import random

vocabs = {'Alcove': 'nook', 'Artificial': 'man-made', 'Nourishment': 'healthy food', 'Augment': 'improve', 'Conscientious': 'aware, careful', 'Dour': 'sad, angry', 'Intimation': 'foreshadowing', 'Lethargic': 'tired, drousy', 'Opulent': 'fancy, excessively good looking', 'Pliable': 'soft, flexible', 'Reiterate': 'to repeat', 'Suitable': 'fitting, correct', 'Tentative': 'uncertain, caucious', 'Unkempt': 'messy', 'Wary': 'cautious, furious'}
print('To switch to learn-mode write "-learn" and to see all vocabs "-list"\n')

def learn():
    while True:
        random_pair = random.choice(list(vocabs.items()))
        if input(f"{random_pair[1]}: ") == random_pair[0]:
            print('Correct')
        else:
            print(f'FALSE, {random_pair[0]}')
        

while True:
    user1 = input(f'#{len(vocabs)} ')
    if user1 == '-learn':
        learn()
    elif user1 == '-list':
        print(vocabs)
    else:
        user2 = input(f'##{len(vocabs)} ')
        vocabs[user1] = user2
        
    