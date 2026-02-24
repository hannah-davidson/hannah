# FILE: homework4.py

# LISTS
# List operations
favorite_foods = ['soup','cheese','chocolate','tomatoes','grapes']
"""
NameError: name 'favorite_foods' is not defined
-> I put a : instead of a = when defining my list.
"""
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append('carrots')
favorite_foods.insert(0,'apple')
favorite_foods.remove(favorite_foods[2])
print(len(favorite_foods))
for food in favorite_foods:
    print(food.upper())
"""
AttributeError: 'list' object has no attribute 'upper'
Apparently, you can't call this function on a list. You can, however, call it for an index, 
so I changed what I am putting before the .upper() to be each index of the list.
"""
print(favorite_foods)
sliced_favorite_foods = [favorite_foods[0], favorite_foods[5]]

for food in sliced_favorite_foods:
    if food == 'potato':
        print('A potato!')
    else:
        print('No potato!')

# Slicing and striding
numbers = list(range(0,21))
def get_first_15(num):
    return num[0:15]
def get_every_5th(lst):
    return lst[::5]
def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(f"Step 1: {step1}")
print(f"Step 2: {step2}")
print(f"Step 3: {step3}")

"""
  File "/Users/hannahdavidson/python_decal_sp26/hannah/homework4/homework4.py", line 44, in <module>
    step3 = reverse_and_stride(step2)
  File "/Users/hannahdavidson/python_decal_sp26/hannah/homework4/homework4.py", line 39, in reverse_and_stride
    reversed_list = lst[::-1]
TypeError: There are no type variables left in list[slice(None, None, 5)]
When  I used list[::5] in get_every_5th, Python tried to create a reusable name for a kind of 
object, rather than returning an actual sliced list.
"""

# Nested Lists
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(numbers[2])
"""
line 62, in <module>
    [1,2,3]
TypeError: list indices must be integers or slices, not tuple
This arose because I forgot to put the comma after each row in the nested list.
"""
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(list):
    count = 0
    for row in list:
        for num in row:
            count += num
    return count

def create_5x5():
    grid = []
    num = 1
    for row in range(5):
        new_row = []
        for col in range(5):
            new_row.append(num)
            num += 1
        grid.append(new_row)
    return grid
five_by_five = create_5x5()

def replace_multiples(lst):
    for row in lst:
        for i in range(len(row)):
            if row[i] % 3 == 0:
                row[i] = '?'
    return lst
print(replace_multiples(five_by_five))

def add_not_equal_to(lst):
    count = 0
    for row in lst:
        for i in range(len(row)):
            if row[i] != '?':
                count += row[i]
    return count
print(add_not_equal_to(five_by_five))

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages['Mariam']

for name, age in ages.items():
    print(name, age)

print(reverse_and_stride(five_by_five))