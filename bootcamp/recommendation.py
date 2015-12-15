import random

restaurants = [
    "Laut",
    "Chipotle",
    "Eataly",
    "Sophie's Cuban",
    "Chop't",
    "Potbelly's",
    "Ootoya"
]

recommendation_history = []


def recommend():
    random.shuffle(restaurants)
    for choice in restaurants:
        # Slice the list starting from the two last element to the end
        if choice not in recommendation_history[-2:]:
            recommendation_history.append(choice)
            return choice
