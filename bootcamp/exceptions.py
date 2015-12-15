

def divide(a, b):
    """
    divide(5, 2) -> 2.5
    """
    try:
        result = a / float(b)
    except (TypeError, ValueError):
        print "Both the numerator and denominator must be valid numbers!"
    except ZeroDivisionError:
        print "We cannot divide by zero!"
    else:
        return result










# string = "20"

# try:
#     number = int(string)
# except ValueError:
#     print "Please enter a valid integer value"
# else:
#     result = {"value": number}
#     print number