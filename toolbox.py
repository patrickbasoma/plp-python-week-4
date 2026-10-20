# Return a number multiplied by 2
def double(number):
    return number * 2


# Return True if the score is 50 or higher
def is_pass(score):
    return score >= 50


# Return a greeting with a default value of "Hello"
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# Test the three functions
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))