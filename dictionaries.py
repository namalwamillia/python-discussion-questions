#Create a dictionary with three key-value pairs representing a student's
#information: name, age, and grade. Print each key-value pair on a new line.


# Create a dictionary with student's information
student = {
    "name": "Alice",
    "age": 24,
    "grade": "A"
}

# Loop through the dictionary and print each key-value pair
for key, value in student.items():
    print(f"{key}: {value}")




#Write a function that takes a dictionary of people's names and their ages,
#{'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of
#people who are 21 or older.


# def get_adults(people):
#     # List comprehension to get names of people who are 21 or older
#     adults = [name for name, age in people.items() if age >= 21]
#     return adults

# #creating a dictionary
# people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}

# # Calling  the function
# adults = get_adults(people)

# print(adults)




# #Given a dictionary representing items in a store with their prices,
# #{'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes
# #a list of items bought, ['apple', 'orange', 'banana', 'banana'], and
# #calculates the total cost.



# # Dictionary of items and their prices
# prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}

# # List of items bought
# items_bought = ['apple', 'orange', 'banana', 'banana']

# # Initialize the total cost to 0
# total_cost = 0

# # Loop through each item in the list of items bought
# for item in items_bought:
#     if item in prices:  # Check if the item is in the price list
#         total_cost += prices[item]  # Add the price of the item to the total cost


# print(f"The total cost of the items is: ${total_cost:.2f}")




# #Write a program that counts the occurrences of each word in a given
# #sentence. Example: for the sentence "hello world hello," the output should be
# #{'hello': 2, 'world': 1}.


# def count_words(sentence):
#     # Convert the sentence to lowercase and split it into words
#     words = sentence.lower().split()
    
#     # Initialize an empty dictionary to store word counts
#     word_count = {}
    
#     # Loop through each word in the list of words
#     for word in words:
#         # Remove any punctuation from the word e.g commas and  periods.
#         word = word.strip(",.?!;:")
        
#         # Update the count of the word in the dictionary
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
    
#     return word_count

# #using the sentence below
# sentence = "hello programmers"

# # Call the function and print the result
# result = count_words(sentence)
# print(result)