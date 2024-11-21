#1. Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ('Mango','Apple','Pawpaw','Orange','Water melon')
for x in fruits:
    print(x)

#. Intermediate: Write a function that takes a list of numbers and returns a new list with
#each number squared. Example: [1, 2, 3] should become [1, 4, 9].

# Function to square each number in the list
def square_numbers(numbers):
    squared_numbers = []  # Create an empty list to store squared numbers
    for number in numbers:  # Loop through each number in the list
        squared_numbers.append(number ** 2)  # Square the number and add to the list
    return squared_numbers  # Return the new list

# Example usage
numbers = [1, 2, 3]
squared_list = square_numbers(numbers)

# Print the result
print(squared_list)

