# File: homework1. py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, consisting of a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, which is any text contained within these quotation marks.

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, which stores data values in key:value pairs.

g = (1,2)
print(g)
print(type(g)) # g is a tuple, which is used to store multiple items in a single variable (immutable).

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, which stores multiple items in a single variable (mutable)

i = True
print(i)
print(type(i)) # i is a boolean, which represents either true or false.

j = None
print(j)
print(type(j)) # j is a NoneType, which is an object that indicates no value.

k = [True, "blue", 12]
print(k)
print(type(k)) # k is also a list.

l = str(14)
print(l)
print(type(l)) # l is a string.

m = 1e4
print(m)
print(type(m)) # m is a float because it has a decimal point.

# 1. I found 9 different data types.
# 2. integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
# 3. e, h, and k are all lists. b and m are both floats. d and l are both strings.
# 4. l is a string, not an integer, because the str() function converts the specified value into a string.
# 5:
n = b"Hello"
print(n)
print(type(n)) # n is bytes, which is a sequence of bytes that cannot be changed that is useful for representing binary data.

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(10<=9) # False, 10 is not less than or equal to 9
(bool("abc")) # True, because it is not an empty string.
bool(123) # True, because it is not a 0 integer.
bool(["apple", "cherry", "banana"]) # True because it is not an empty list.
bool(True) # True; it is an explicit output of boolean value True, so it remains true.
bool(False) # False; it is an explicit output of the boolean value False, so it remains false.
bool(0) # False, beacuse it is a 0 integer.
bool("") # False, because it is an empty string.
bool(" ") # True, because it is not an empty string.
bool(()) # False, because it is an empty tuple.
print(bool([])) # False, because it is an empty list.
bool({}) # False, because it is an empty dictionary.
bool(True and False) # False; the and operator only returns True if both of its operands are true.
bool(True and True) # True; the and operator only returns True if both of its operands are true.
bool(False and False) # False; the and operator only returns True if both of its operands are true.
bool(True or False) # True; the or operator only requires one operand to be True to return True.
bool(True or True) # True; the or operator only requires one operand to be True to return True.
bool(False or False) # False; the or operator only requires one operand to be True to return True, otherwise it is false.
bool(not(False)) # True, because it is the opposite of false.
bool(not(True)) # False, because it is the opposite of true.

# Expressions returning True are usually nonempty datatypes, while expressions returning False usually are empty.
# I was surprised that bool(" ") returned True; I was not expecting a space to count as a non-empty value.
# bool(False or True or False) returns True because there is one True operand.
# bool((())) returns False because it is empty.

# --- Operators ---
# -- Arithmetic Operators --
10 + 5 # 15, + performs addition
10 - 5 # 5, - performs subtraction
2*4, # 8, * performs multiplication
6/3 # 2.0, / performs division and returns a float.
5 % 2 # 1, performs division and returns the remainder.
3 ** 2 # 9, performs exponentiation.
15 // 2 # 7, performs integer division, not giving the remainder.
# -- Comparison Operators --
5 == 2 # False, == means equals
10 != 10 # False, != means does not equal
2 < 5 # True, < means less than
12 > 5 # True, > means greater than
5 <= 6 # True, <= means less than or equal to 
1 >= 10 # False, >= means greater than or equal to
# -- Assignments Operators --
x = 5
x += 5 # 10, adds 5 to the given amount initially assigned to x
x -= 4 #1, subtracts 4 from given amount initially assigned to x
x *= 3 # 15, multiplies given amount intially assigned to x by 3
# -- Logical Operators --
# 1. and is a logical operator that only returns True if both conditions are true.
5 > 3 # True
5 < 3 # False
# 2. or is a logical operator that returns True if one of the conditions is true.
bool(True or False) # True
bool(False or False) # False
# 3. the not operator reverses the boolean truth value of an expression.
bool(not("")) # returns True
bool(not(" ")) # returns False
# - More Questions -
# 1. The / is true division and returns a float, while // returns a rounded integer.
# 2. % returns the remainder of the division, while // returns a rounded-down quotient.
# 3. You would use %. For instance, if you ran 5 % 2, like in the example given, it would return 1, which is the remainder.
# 4. Assignment operators assign values to variables.

# --- Strings ---
my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints h
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o
print(my_string[1:3]) # prints 'el'
print(my_string[0:5:2]) # prints 'hlo'
print(len(my_string)) # returns 5, which is how many letters there are in the word.
print(my_string + "goodbye") # prints hellogoodbye
print(7*my_string) # prints 'hello' 7 times over

# 1. Slicing extracts a portion of a list, tuple or string. Examples of this manipulation were print(my_string[1:3]) and print(my_string[0:5:2]).
# 2. Returns Hello, my name is Oski.
name = "Oski"
print("Hello, my name is", name)
# # 3. Returns Hello, my name is Oski.
name = "Oski"
print(f"Hello, my name is {name}")
# # 4. the latter statement uses an f-string, which allows you to easily format objects into strings.

# --- 3.5 Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists the contents of a directory
# Example: ls homework1

# ls -a
# Lists all files in a specified directory/current working directory
# Example: ls -a homework1

# mkdir
# Creates directory.
# Example: mkdir homework 1

# cat
# Tells your computers to print out all the contents of a file
# Example: cat homework1.py

# pwd
# Prints working directory
# Example: if in directory homework1, running pwd will return 'homework 1'.

# cd ..
# Moves up one parent directory
# Example: if in homework1, running this command will move me into python_decal_sp26.

# cd ~
# Returns you to highest parent directory
# Example: running this commands returns me to /Users/hannahdavidson.

# cp
# Duplicates files or directories from one location to another within the file system
# Example: cp homework1.py /Users/hannahdavidson/Downloads

# mv
# Moves files and directories from one location to another
# Example: mv homework1.py /Users/hannahdavidson/Downloads

# rm
# Removes files/directories
# Example: rm homework1.py will delete the folder.

# clear
# clears the terminal
# Example: if you want to remove the clutter in your terminal, run 'clear' to clean it out.

# grep
# Acronym for global regular expression print; used to search for tect from a file or another command's output.
# Example: grep "world" homework1.py will show where 'world' is in my file.

# 1. 
# whoami
# Shows the user you are logged in as
# Example: running whoami returns hannahdavidson on my computer.
# date
# Returns date and time in current time zone.
# Example: running date returns Thu Jan 29 10:30:53 PST 2026
# open
# Opens folders, files, URLs
# Example: running open http://google.com opens the Google website.

# 2. ls -a lists all directory contents including hidden files, while ls does not show hidden files.
# 3. A hidden file is an object excluded from a directory content listing unless explicitly called.
# 4. ls -r lists contents in reverse order. rm -i removes a directory, but asks before. ls -l is a long listing, which gives the list contents with more information.

