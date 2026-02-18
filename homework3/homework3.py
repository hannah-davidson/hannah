# File: Homework 3 - Functions, Conditionals, and Loops

# PRINT FUNCTIONS
# 3.1 Say Goodbye
def say_goodbye(name):
     print("Goodbye, ", name)
# say_goodbye("Grader")

# 3.2 Area of a Cirlce
def circle_area(radius):
    print(3.14*(radius)**2)
# circle_area(3)

# RETURN FUNCTIONS
# 4.1 Subtract, Multiply, and Divide
def subtract(a,b): # subtracts two numbers
    return a - b
# print(subtract(5,2))

def multiply(a,b): # multiplies two numbers
    return a*b
#print(multiply(5,2))

def divide(a,b): # divides one number by another
    return a/b
#print(divide(5,2))

# CONDITIONALS
# 5.1 What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]
def highs_lows(temperatures):
    return f"The high is {max(temperatures)} and the low is {min(temperatures)}."
#print(highs_lows(readings))

# 5.2 Check if it's the Weekend
def is_weekend(day):
    if day > 5:
        return True
    else:
        return False
#print(is_weekend(6))

# # 5.3 Fuel Efficiency Calculator
def fuel_efficiency(miles, gallons):
    return miles/gallons
miles = 50
gallons = 4
#print(fuel_efficiency(miles, gallons))

# 5.4 Secret Code
def encrypt(n):
    last_digit = n % 10 # Extract last digit using modulus
    remaining = n // 10 # Remove last digit using floor division
    digits = len(str(remaining)) # Count remaining digits to know what power of 10 to shift by
    return last_digit * (10 ** digits) + remaining # Prepend last digit
#print(encrypt(1738))

# LOOPS
# 6.1 Oski Stole Your Power
def exponentiate(x,y):
    result = 1
    for _ in range(y):
        result *= x
    return result # remember to put return statements outside of the loop!   
#print(exponentiate(4, 2))


# Min + Max with Loops
numbers = [14,10,34,34,1,6]
def minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
def maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
# print(minimum(numbers))
# print(maximum(numbers))

def min_val(numbers):
    min = numbers[0]
    i = 1
    while i < len(numbers):
         if numbers[i] < min:
            min = numbers[i]
         i += 1
    return min

def max_val(numbers): # Define a function that takes a list of numbers as an input.
    maximum = numbers[0] # Assume the first index is the smallest to start.
    i = 1 # Start at index 1 since index 0 was used above.
    while i < len(numbers): # Keep looping as long as i hasn't reached the end of the list
        if numbers[i] > maximum: # Check if current element is bigger than maximum
            maximum = numbers[i] # If true, update maximum to bigger value.
        i += 1 # Move to next index.
    return maximum
# print(min_val(numbers))
# print(max_val(numbers))

def sum_digits(integer):
    sum = 0
    for digit in str(integer):
        sum += int(digit)
    return sum
#print(f"The sum of the digits of 1738 is {sum_digits(1738)}.")