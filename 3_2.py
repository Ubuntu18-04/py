import random as r
deck=["Spade","Heart","Diamond","Club"]
print("Deck before shuffling:",deck)
r.shuffle(deck)
print("The deck after shuffling=",deck)
print("The random choice=",r.choice(deck))
print("The random sample of 2=",r.sample(deck,2))