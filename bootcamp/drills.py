

def tally(food_orders):

    # Initialize result dict
    result = {}

    # Loop over the orders
    for order in food_orders:

        # If current order in result, then increment value by 1
        if order in result:
            result[order] += 1
        # If new order, set key-value pair in result to 1
        else:
            result[order] = 1

    # Return result dict
    return result


def top_x(orders, number):

    # Get list of tuples (key-value pairs)
    # e.g. [('burger', 3), ('fries', 2), ...]
    food_tuples = tally(orders).items()

    # Sort by frequency
    food_tuples_sorted = sorted(
        food_tuples,
        key=lambda x: x[1],
        reverse=True)

    return food_tuples_sorted[:number]


print top_x(['burger', 'burger', 'burger', 'fries', 'ice_cream', 'fries'], 2)
