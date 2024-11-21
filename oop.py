#1.Create a class called Car with attributes brand and color. Instantiate an object
#of the Car class and print its attributes.

#Define the Car class
class Car:
    def __init__(self, brand, color):
        # Initialize the attributes
        self.brand = brand
        self.color = color

# Instantiate an object of the Car class
my_car = Car("Toyota", "Red")

# Print the attributes of the car
print(f"Car brand: {my_car.brand}")
print(f"Car color: {my_car.color}")



#2.Add a method called start_engine to the Car class that prints a
#message saying the engine of the car has started. Create an instance of Car and call
#the method.

# Define the Car class with an additional method
class Car:
    def __init__(self, brand, color):
        # Initialize the attributes
        self.brand = brand
        self.color = color

    
    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started!")

# Instantiate an object of the Car class
my_car = Car("Toyota", "Red")

# Calling  the start_engine method
my_car.start_engine()







#3.Create a class called BankAccount with attributes account_number and
#balance. Add methods to:
#○ Deposit an amount.
#○ Withdraw an amount (only if sufficient balance exists).
#○ Print the account balance.


class BankAccount:
    def __init__(self, account_number, balance=0):
        
        # Initialize account attributes
        self.account_number = account_number
        self.balance = balance

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

   
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be greater than 0.")

    
    def print_balance(self):
        print(f"Account balance: ${self.balance}")



#4.Create an account with a starting balance of 1000
account = BankAccount("123456789", 1000)  

# Deposit and withdraw some amounts, and print balance

# Deposit $500
account.deposit(500)


# Withdraw $200
account.withdraw(200)
  
  #print the final balance
account.print_balance()

# Attempt to withdraw more than available balance

account.withdraw(1500)  


#Implement a class called Library that manages a collection of books. Each
#book has a title, author, and available status. The Library class should have
#methods to:
#○ Add a book to the library.
#○ Remove a book from the library.
#○ Check if a book is available by title.
#○ Borrow a book (mark it as unavailable if it’s available).
#○ Return a book (mark it as available again if it was borrowed).


class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    
    def add_book(self, title, author):
        book = {
            'title': title,
            'author': author,
            'available': True  
        }
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    #to remove a book from the library by title
    def remove_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")
        
        

    #to check if a book is available by title
    def check_availability(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                if book['available']:
                    print(f"Book '{title}' is available.")
                else:
                    print(f"Book '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")
        
        

    # Method to borrow a book (mark it as unavailable)
    def borrow_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                if book['available']:
                    book['available'] = False
                    print(f"You have borrowed the book '{title}'.")
                else:
                    print(f"Book '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")



    # Method to return a book 
    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                if not book['available']:
                    book['available'] = True
                    print(f"You have returned the book '{title}'.")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")
        
        

    #Display the list of all books 
    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                status = "Available" if book['available'] else "Unavailable"
                print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")
        else:
            print("No books in the library.")


library = Library()

# Add books
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Display all books
library.display_books()

# Check availability
library.check_availability("1984")

# Borrow a book
library.borrow_book("1984")

# Check availability again
library.check_availability("1984")

# Return a book
library.return_book("1984")

# Remove a book
library.remove_book("The Great Gatsby")

# Display books after removal
library.display_books()