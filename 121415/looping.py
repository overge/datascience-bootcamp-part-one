

def count_numbers(numbers):
    counter = 0
    for number in numbers:
        # counter = counter + 1
        counter += 1

    return counter

counter = 4
print count_numbers([1, 2, 4, 7, 8, 9])
print counter


disney = ["Donald Duck", "Mickey Mouse", "Daffy Duck", "Goofy", "Minnie Mouse", "Pluto"]
list_a = [x for x in disney if "a" in x]
list_u = [x for x in disney if "u" in x]
