'''
In Python when we use the addition operator (+) with two strings it concatenates them, meaning it just combines the strings.
'''
print("dog" + "cat")
print("5" + "10")

'''
Remember: All input is returned as a String regardless of what was inputted.
If you want to do math with any user input you must type cast the data type to a type of data that you can do math with such as an Integer or Float.
Type casting does not change the data type of the original variable, but it will treat it as such for a single line of code.
In this example, we use the int() function to cast the input to the type Integer.
'''
# num1 = int(input("Please enter a number: ")) 
# num2 = int(input("Please enter another number: "))
# print(num1 + num2)


'''
When you use the addition operator (+) in Python, both sides of the equation must have the same data type, otherwise it will not compile, and it will generate an error.
You can utilize a concept here called Type Casting where we forcibly treat a value as if it is of another data type to resolve this.
For example, we can cast something to the type String with the str() function, or we can cast something to the type Integer with the int() function. 
'''
print(int("100") + 100)
print("100" + str(100))

'''
If you need to print values of multiple different data types in a single print() statement, it is recommended that you use print(f) because this can allow you
to print out different data types without type casting.
'''
string = "Test"
number = 500

print(f"The value of string is {string} and the value of number is {number}")