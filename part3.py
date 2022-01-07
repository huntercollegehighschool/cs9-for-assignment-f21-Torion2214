"""
******
PART 3
******

Write a program that prompts the user to enter two integers, one representing the base of a rectangle, and one representing the height. The program will then print a rectangle made of asterisks (*) with those dimensions. 

(Hint: this may involve nested for loops(ie. a for loop inside a for loop), but it does not have to. Concatenating/adding strings ('*' + '*') or replicating strings ('*' * 3) may be helpful here.)

An example of what should appear on the console when the program runs:

Enter the base: 7
Enter the height: 3

*******
*******
*******

"""

num1 = int(input("Enter the base: "))
num2 = int(input("Enter the height: "))

for x in range (1,num2 +1):
  for y in range (1,num1 +1):
    print ('*', end = "")
  print ()