#monte carlo example blackjack
import random
"""
def dealHand():
    deck = (list(range(1,11)) + [10,10,10]) * 4
    random.shuffle(deck)
    return (deck[0:2])

TRIALS = 100000
wins = 0
for i in range(TRIALS):
    hand = dealHand()
    if 1 in hand and 10 in hand:
        wins += 1

print(wins/TRIALS)
        

#second example boardgame
def roll():
    die1 = ["eye", "eye", "eye", "paw", "paw", "paw"]
    die2 = ["eye", "eye", "eye", "paw", "paw", "paw"]
    die3 = ["eye", "eye", "eye", "paw", "paw", "paw"]

    r1 = random.choice(die1)
    r2 = random.choice(die2)
    r3 = random.choice(die3)
    results = [r1, r2, r3]
    if "paw" not in results:
        return True
    if r1 == "paw":
        r1 = random.choice(die1)
    if r2 == "paw":
        r2 = random.choice(die2)
    if r3 == "paw":
        r3 = random.choice(die3)
    results = [r1, r2, r3]
    if "paw" not in results:
        return True
    if r1 == "paw":
        r1 = random.choice(die1)
    if r2 == "paw":
        r2 = random.choice(die2)
    if r3 == "paw":
        r3 = random.choice(die3)
    results = [r1, r2, r3]
    if "paw" not in results:
        return True
    return False




TRIALS = 100000
wins = 0
for i in range(TRIALS):
    if roll():
        wins += 1

print(wins/TRIALS)

"""

def roll():
    die1 = ["Red", "Green", "Blue", "Yellow"]
    red = 0
    green = 0
    blue = 0
    yellow = 0
    total_fruit = 0
    raven = 0
    r1 = random.choice(die1)
    for i in range(100): 
        if r1 == "Red":
            if red <= 4:
                red += 1
                total_fruit += red
        if r1 == "Green":
            if green <= 4:
                green += 1
                total_fruit += green
        if r1 == "Blue":
            if blue <= 4:
                blue += 1
                total_fruit += blue
        if r1 == "Yellow":
            if yellow <= 4:
                yellow += 1
                total_fruit += yield
        return total_fruit
print(roll())
    







"""
TRIALS = 100000
wins = 0
for i in range(TRIALS):
    if roll():
        wins += 1

print(wins/TRIALS)


"""













    
