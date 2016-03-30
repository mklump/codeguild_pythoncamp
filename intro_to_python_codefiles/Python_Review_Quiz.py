#1. Print “Hello World”
print('Hello World')

#2. Create a list called fruit that has Apples, Oranges and Bananas as values.
fruit = ["Apples", "Oranges", "Bananas"]

#3. Print the list.
print(fruit)

#4. Change Oranges to Grapes using the numeric list index.
fruit[1] = "Grapes"

#5. Create a loop that prints out each item in the fruit list.
for fruitItem in fruit:
    print(fruitItem + " ")

#6. Create a dictionary called people that has another dictionary for each Bob (age 22), Carol (age 47) and Justin (age 14) with their name and age.
people = { Bob = { "age" : 22 }, Carol = { "age": 47 }, Justin = { "age" : 14} }

#7. Create a function that takes two numbers (a and b) and prints the total value when they are added.
import numbers
def fuction1(a, b):
    if True == isinstance(a, numbers.Number) and True == isinstance(b, numbers.Number):
        return a + b
    else
        print("Add Error: Either parameter a or b is not a number.")

#8. Call your function with 5 and 5, 10 and 15 and 3 and 6.
print("Calling function1(5, 5), and the result is %d" % function1(5, 5))
print("Calling function1(10, 15), and the result is %d" % function1(10, 15))
print("Calling function1(3, 6), and the result is %d" % function1(3, 6))

#9. Create a function that takes user input of an integer and loops through printing that number plus 5 until it reaches 1000.
def function2():
    intNum = raw_input("Enter an integer to add 5 to until it reaches 1000 : ")
    if False == isinstance(intNum, numbers.Integer):
        print("The entry you provided is not an integer.")
    else if intNum > 1000:
        print("The integer you provided should be less than 1000 for a proper printed summation.")
    print("That integer and the printed summation is:")
    for i in range(intNum, 1000):
        print(format("%d, ", i))
        i += 5 # I understand the fact this will more than likely be incremented a second time, and need to use an iter iterator object insted

#10. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 100):
    if 0 == i % 3:
        print("Fizz")
    else if 0 == i % 5:
        print("Buzz")
    else if 0 == i % 3 and 0 == i % 5:
        print("FizzBuzz")
