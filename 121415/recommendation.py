import random

restaurants = ["Laut", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

def recommend():
    random.shuffle(restaurants)
    print restaurants[0]

recommend()