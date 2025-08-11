# program to calculate the average of two numbers
# take two numbers as input
num1= float(input("enter the first number"))
num2 = float(input("enter the second number"))
# declare average = ( num1 + num2)
average = (num1 + num2) /2
# accept an age input from the user and a full name
age = int(input("what is your age"))
full_name = input("what is your full name")
# if the age is less than the 18 and the average is equal to 20
if age < 18 and int(average) == 20:
    print(f"{full_name} you are allowed to vote")
# if the age is greater than or equal to 18 and the average is greater than or equal to 20 print {name} you are allowed to vote
if age >= 18 and average >= 20:
    print(f"{full_name} you are allowed to vote")
   