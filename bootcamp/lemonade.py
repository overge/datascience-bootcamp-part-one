# Express assumptions
lemons_per_lemonade = 4
cost_per_lemon = 0.5
revenue_per_lemonade = 5

cost_per_lemonade = cost_per_lemon * lemons_per_lemonade
profit_per_lemonade = revenue_per_lemonade - cost_per_lemonade


# Collect user input (num_lemonades, num_hours)
num_lemonades = int(raw_input("How many lemonades did you sell? "))
num_hours = float(raw_input("How many hours did it take? "))

# Calculate profit and profit per hour
profit = num_lemonades * profit_per_lemonade
profit_per_hour = profit / num_hours

# Print results
print "You made ${} by selling {} lemonades in {} hours, that is ${} per hour.".format(
    profit, num_lemonades, num_hours, profit_per_hour)
