
# IB DP CompSci - First Class Exercise: Data Types

# For each variable below, write a comment with what kind of thing it is (int, float, str, or bool)
number = 7          # Creating a VARIABLE and ASSIGNING a VALUE to it
decimal = 3.5
word = "hello"
is_sunny = True
number_type = type(number)      # ASSIGNING the TYPE of the variable to a new variable
decimal_type = type(decimal)
word_type = type(word)
is_sunny_type = type(is_sunny)
print(number_type)      # PRINTING the TYPE to the console
print(decimal_type)
print(word_type)
print(is_sunny_type)

# Change the values to the type shown in the comment by adjusting how the value is written
# (hint: strings are in quotes, booleans are True/False, floats have a decimal point, integers are whole numbers)

age = "15"      # Change to int
score = 10      # Change to str
rain = "False"  # Change to bool
height = "1.75" # Change to float

# Test your changes by printing the types to the console
print(type(age))
print(type(score))
print(type(rain))
print(type(height))

# What will be printed?
print(type(2 + 2))
print(type("5" + "5"))
print(type(3.0 + 1))
print(type(True))
# Write your guesses as comments, then run and check
