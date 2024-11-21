#qn.1)Basic: Write a Python program that prints all even numbers between 1 and 20 using a
#for loop.

def numBetweenOneToTen():
  for  even in range(2,20,2):
      print(even)
      
numBetweenOneToTen()

#2. Intermediate: Use a while loop to ask the user to input a number until they provide a
#number greater than 10
i = 1
while i < 12:
 print(i)
 i +=1 
      
#3.Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers
#from 1 to 5 using nested for loops.
#Outer loop for numbers from 1 to 10

for i in range(1,6):
    print(f"Multiplication table for {i}:")
    
#inner loop for numbers from 1  to 10
    for j in range(1, 11):
    
       print(f"{i} * {j} = {i * j}")
    
    print()
    
# 4.Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a
#for loop to find the sum of all odd numbers and print the result.
#list numbers
list = [4, 7, 2, 9, 12, 15]
#initialize sum of odd numbers in list to 0
sum_of_odd = 0

#loop through the list
for  number in list:
     #check  if the number is odd
     if  number % 2 != 0:
     
        sum_of_odd  += number
    
    # print sum of odd numbers
print(" The sum of odd number:",sum_of_odd )
    

