#Python Assignment

#SECTION 1: PRINT & OUTPUT (10 Questions) 
#1. Print your name, age, and city in a single formatted sentence.
#2. Print numbers from 1 to 10 in a single line separated by space.
#3. Print a multiplication table for a given number (e.g., 7).
#4. Print a right-angle triangle star pattern (5 rows).  
#5. Print the sum of first 20 natural numbers.  
#6. Print all odd numbers between 1 and 50.  
#7. Print a string in reverse using print statement logic.  
#8. Print two strings on the same line using a custom separator.  
#9. Print output using escape characters (newline, tab).  
#10. Print the result of arithmetic operations inside a formatted string.  

#SECTION 2: VARIABLES & DATA TYPES (10 Questions) 
#11. Declare variables for name, age, and salary and print them. 
#12. Swap two variables without using a third variable.  
#13. Take user input and print it with a greeting message.  
#14. Assign multiple variables in one line and print their sum.  
#15. Check and print the data type of a variable.  
#16. Convert a string number into an integer and perform addition.  
#17. Convert an integer into a string and concatenate with another string.  
#18. Create variables of int, float, string, and boolean and print their types.  
#19. Reassign a variable with a different data type and print the result.  
#20. Write a program to calculate simple interest using variables.  

#SECTION 3: OPERATORS (10 Questions) 
#21. Perform all arithmetic operations on two numbers.  
#22. Find the remainder when one number is divided by another.  
#23. Calculate the power of a number using an operator.  
#24. Use floor division to divide two numbers and print the result.  
#25. Compare two numbers and print which one is greater.  
#26. Check if a number is even or odd using operators.  
#27. Use logical operators to check if a number lies between 10 and 50.  
#28. Use assignment operators (+=, -=, etc.) and print updated values.  
#29. Check if a number is divisible by both 3 and 5.  
#30. Write a program to find the largest of two numbers using operators.  

#SECTION 4: INTEGERS & DECIMALS (10 Questions) 
#31. Add an integer and a float and print the result.  
#32. Convert a float value into an integer and print it.  
#33. Divide two numbers and print the decimal result.  
#34. Round a decimal number to 2 decimal places.  
#35. Format a float to display only 3 decimal points.  
#36. Check whether a variable is of type integer.  
#37. Find the absolute value of a negative number.  
#38. Multiply two decimal numbers and print the result.  
#39. Convert a decimal number into a string.  
#40. Calculate the average of three numbers (including decimals).  

#SECTION 5: MIXED QUESTIONS  
#41. Create a simple calculator using basic operators.  
#42. Convert temperature from Celsius to Fahrenheit.  
#43. Check whether a number is positive, negative, or zero.  
#44. Find the sum of digits of a number.  
#45. Calculate the area of a circle using variables and float values.  
#46. Find the square and cube of a number.  
#47. Write a program to calculate the perimeter of a rectangle.  
#48. Take two decimal inputs and print their product.  
#49. Check if two numbers are equal using comparison operators. 
#50. Write a program to calculate the average of 5 user-input numbers. 

#################################################################################################################################################
################################   ANSWERS           ###########################################
#################################################################################################################################################

#1. Print your name, age, and city in a single formatted sentence.

name = 'Duraipandian'
age = 29
city = "chennai"
print("#################################################################")
print("1. Print your name, age, and city in a single formatted sentence.")
print("#################################################################")

print(f'I  am {name} ,{age} years old and from {city}')
print()


#2. Print numbers from 1 to 10 in a single line separated by space.

print("#################################################################")
print("2. Print numbers from 1 to 10 in a single line separated by space.")
print("#################################################################")

print("1 2 3 4 5 6 7 8 9 10")
print()

#3. Print a multiplication table for a given number (e.g., 7).

print("#################################################################")
print("3. Print a multiplication table for a given number (e.g., 7).")
print("#################################################################")

table_number=int(input("Please enter table number:"))

print(f"1 * {table_number} = ",1*table_number)
print(f"2 * {table_number} = ",2*table_number)
print(f"3 * {table_number} = ",3*table_number)
print(f"4 * {table_number} = ",4*table_number)
print(f"5 * {table_number} = ",5*table_number)
print(f"6 * {table_number} = ",6*table_number)
print(f"7 * {table_number} = ",7*table_number)
print(f"8 * {table_number} = ",8*table_number)
print(f"9 * {table_number} = ",9*table_number)
print(f"10 * {table_number} = ",10*table_number)
print(f"11 * {table_number} = ",11*table_number)


print()


#4. Print a right-angle triangle star pattern (5 rows).  
print("#################################################################")
print("4. Print a right-angle triangle star pattern (5 rows).")
print("#################################################################")

print("    *")
print("   **")
print("  ***")
print(" ****")
print("*****")
print()


#5. Print the sum of first 20 natural numbers.  
print("#################################################################")
print("5. Print the sum of first 20 natural numbers.")
print("#################################################################")

print( 1+ 2+ 3+ 4+ 5+ 6+ 7+ 8+ 9+ 10+ 11+ 12+ 13+ 14+ 15+ 16+ 17+ 18+ 19+ 20)
print()

#6. Print all odd numbers between 1 and 50.  

print("#################################################################")
print("6. Print all odd numbers between 1 and 50.")
print("#################################################################")

print("1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49")

print()

#7. Print a string in reverse using print statement logic.  

print("#################################################################")
print("7. Print a string in reverse using print statement logic.")
print("#################################################################")

reverse_string ="Duraipandian"
print(reverse_string[::-1])

print()

#8. Print two strings on the same line using a custom separator.  

print("#################################################################")
print("8. Print two strings on the same line using a custom separator.")
print("#################################################################")

string1="GenAI"
string2="python"

print(string1,string2,sep="---")
print()


#9. Print output using escape characters (newline, tab).  
print("#################################################################")
print("9. Print output using escape characters (newline, tab).")
print("#################################################################")

print("Hi\tstudent Welcome\tto\tTechpanda\nPython\tcourse")
print()

#10. Print the result of arithmetic operations inside a formatted string.  
print("#################################################################")
print("10. Print the result of arithmetic operations inside a formatted string")
print("#################################################################")

a,b =30,20
print(f"Arithmetic opertion of addition a,b is {a+b}")
print(f"Arithmetic opertion of subtraction a,b is {a-b}")
print(f"Arithmetic opertion of Mutliplication a,b is {a*b}")
print(f"Arithmetic opertion of Division a,b is {a/b}")
print(f"Arithmetic opertion of Modulus a,b is {a%b}")
print()


#11. Declare variables for name, age, and salary and print them. 

print("#################################################################")
print("11. Declare variables for name, age, and salary and print them")
print("#################################################################")

NAME = "Duraipandian"
AGE = 29
Salary = 35000

print(f"Name = {NAME} \nAge = {AGE} \nSalary = {Salary}")
print()


#12. Swap two variables without using a third variable.  

print("#################################################################")
print("12. Swap two variables without using a third variable")
print("#################################################################")

a,b=10,20
print(f"Before swap a is {a} and b is {b}")
a=a+b
b=a-b
a=a-b
print(f"After swap a is {a} and b is {b}")

print()


#13. Take user input and print it with a greeting message.  


print("#################################################################")
print("13. Take user input and print it with a greeting message.")
print("#################################################################")

Greeting_name = input("Please Enter greeting message name:")

print(f"Hi {Greeting_name}. Welcome to Techpanda Python Class")
print()


#14. Assign multiple variables in one line and print their sum.  


print("#################################################################")
print("14. Assign multiple variables in one line and print their sum.")
print("#################################################################")


a ,b,c = 10, 20, 30
print("Sum of Mutliple variable declared in single line :", a+b+c)
print()

#15. Check and print the data type of a variable.  



print("#################################################################")
print("15. Check and print the data type of a variable.")
print("#################################################################")


interger = 1
string = "durai"
float_number = 23.23
boolean_type= True
list_type = [12,14,25,53]
tuple_type = (12,24,53,31)

print("Data Type of variable int,str,float,boolean,list,tuple",type(interger),type(string),type(float_number),type(boolean_type),type(list_type),type(tuple_type))
print()



#16. Convert a string number into an integer and perform addition.  


print("#################################################################")
print("16. Convert a string number into an integer and perform addition.")
print("#################################################################")


a,b ='23','45'
print(type(a),type(b))

print("Addition of two string interger covert into int",int(a)+int(b))
print()


#17. Convert an integer into a string and concatenate with another string.  

print("#################################################################")
print("Convert an integer into a string and concatenate with another string.")
print("#################################################################")


int_str = 12345
letter = "durai"

print("Convert an integer into a string and concatenate with another string.",str(int_str)+letter)
print()


#18. Create variables of int, float, string, and boolean and print their types.  


print("#################################################################")
print("18. Create variables of int, float, string, and boolean and print their types.")
print("#################################################################")

interger1 = 1
string1 = "durai"
float_number1 = 23.23
boolean_type1= True
list_type1 = [12,14,25,53]
tuple_type1 = (12,24,53,31)

print("Data Type of variable int,str,float,boolean,list,tuple",type(interger1),type(string1),type(float_number1),type(boolean_type1),type(list_type1),type(tuple_type1))
print()


#19. Reassign a variable with a different data type and print the result.  


print("#################################################################")
print("19. Reassign a variable with a different data type and print the result.")
print("#################################################################")


number = 12345
print("Before reassign number variable is:",number)
number = "durai"
print("After re-assign number int variable into string",number)
print()

#20. Write a program to calculate simple interest using variables.  

print("#################################################################")
print("20. Write a program to calculate simple interest using variables.  ")
print("#################################################################")

Principal=int(input("Please Enter Principal Amount:"))
Rate=int(input("Please Enter Rate of interest:"))
time=int(input("Please Enter Number of years:"))

simple_interest = (Principal * Rate * time) / 100
print(f"Simple Interset is {simple_interest}")
print()

#21. Perform all arithmetic operations on two numbers.  

print("#################################################################")
print("21. Perform all arithmetic operations on two numbers.")
print("#################################################################")


a,b =100,50
print(f"Arithmetic opertion of addition a,b is {a+b}")
print(f"Arithmetic opertion of subtraction a,b is {a-b}")
print(f"Arithmetic opertion of Mutliplication a,b is {a*b}")
print(f"Arithmetic opertion of Division a,b is {a/b}")
print(f"Arithmetic opertion of Floor Division a,b is {a//b}")
print(f"Arithmetic opertion of Modulus a,b is {a%b}")
print(f"Arithmetic opertion of Exponential a,b is {a**b}")
print()

#22. Find the remainder when one number is divided by another.  

print("#################################################################")
print("22. Find the remainder when one number is divided by another.  ")
print("#################################################################")

a,b=10,20

print("Remainder of number a=10,b=20 is ",a%b)
print()

#23. Calculate the power of a number using an operator.  

print("#################################################################")
print("23. Calculate the power of a number using an operator.")
print("#################################################################")

a,b=5,2
print("Power of a number is",a**b)
print()

#24. Use floor division to divide two numbers and print the result.  

print("#################################################################")
print("24. Use floor division to divide two numbers and print the result.")
print("#################################################################")

a,b=10,20
print("Floor division of two number is:",a//b)
print()

#25. Compare two numbers and print which one is greater.  

print("#################################################################")
print("25. Compare two numbers and print which one is greater.")
print("#################################################################")


a=int(input("Please enter a number a is:"))
b=int(input("Please enter a number b is:"))

if a<b:
    print("B is greater than a, B value is ",b)
else:
    print("A is greater than B, A vaule is ",a)

print()

#26. Check if a number is even or odd using operators.  

print("#################################################################")
print("26. Check if a number is even or odd using operators.  ")
print("#################################################################")

Number=int(input("Please enter a number:"))

if Number % 2 == 0:
    print("Given number is Even.Number is :",Number)
else:
    print("Given number is odd number.Number is:",Number)

print()


#27. Use logical operators to check if a number lies between 10 and 50.  

print("#################################################################")
print("27. Use logical operators to check if a number lies between 10 and 50.")
print("#################################################################")

a=int(input("Please enter a number:"))

if a>=10 and a<=50:
    print("Entered number lies between 10 and 50 ,Number is",a)
else:
    print("Entered number Not lies between 10 and 50 ,Number is",a)

print()

#28. Use assignment operators (+=, -=, etc.) and print updated values.  

print("#################################################################")
print("28. Use assignment operators (+=, -=, etc.) and print updated values.")
print("#################################################################")

a,b=10,20
print("Value of a and b is:",a,b)
a+=b
print("added a plus b stored in a itself:",a)
a-=b
print("added a minus b stored in a itself:",a)

print()



#29. Check if a number is divisible by both 3 and 5.  
print("#################################################################")
print("29. Check if a number is divisible by both 3 and 5.")
print("#################################################################")

Num=int(input("Please enter a number:"))

if Num % 3 == 0 and Num % 5 == 0:
    print("Number is divisible by both 3 and 5 :given number is",Num)
else:
    print("Number is not divisble by both 3 and 5 : given number is",Num)

print()

#30. Write a program to find the largest of two numbers using operators.  

print("#################################################################")
print("30. Write a program to find the largest of two numbers using operators.")
print("#################################################################")



a=int(input("Please enter a number a is:"))
b=int(input("Please enter a number b is:"))

if a<b:
    print("B is greater than a, B value is ",b)
else:
    print("A is greater than B, A vaule is ",a)

print()



#31. Add an integer and a float and print the result.  
#32. Convert a float value into an integer and print it.  
#33. Divide two numbers and print the decimal result.  
#34. Round a decimal number to 2 decimal places.  
#35. Format a float to display only 3 decimal points.  
#36. Check whether a variable is of type integer.  
#37. Find the absolute value of a negative number.  
#38. Multiply two decimal numbers and print the result.  
#39. Convert a decimal number into a string.  
#40. Calculate the average of three numbers (including decimals). 

#31. Add an integer and a float and print the result.  

print("#################################################################")
print("31. Add an integer and a float and print the result.")
print("#################################################################")


int_num=int(input("Please enter a int number:"))
float_num=float(input("Please enter a float number:"))

print("Addition of int and float number is :",int_num+float_num)

print()

#32. Convert a float value into an integer and print it.

print("#################################################################")
print("32. Convert a float value into an integer and print it.")
print("#################################################################")

float_value = 25.3423
print("Float number converted into interger number :",int(float_value))

print()

#33. Divide two numbers and print the decimal result.  

print("#################################################################")
print("33. Divide two numbers and print the decimal result.")
print("#################################################################")



a=int(input("Please enter a number:"))
b=int(input("Please enter a number:"))

print("Divided two number and result decimal :",float(a/b))

print()


#34. Round a decimal number to 2 decimal places.  

print("#################################################################")
print("34. Round a decimal number to 2 decimal places.")
print("#################################################################")


decimal_number = 237.34724
print(f"Round of decimal number to 2 decimal place original number :{decimal_number} and result is : ",round(decimal_number,2))
print()


#35. Format a float to display only 3 decimal points.  


print("#################################################################")
print("#35. Format a float to display only 3 decimal points.")
print("#################################################################")


float1=12.123435
print(f"Original float number {float1} and display only 3 decimal point is: ",round(float1,3))
print()


#36. Check whether a variable is of type integer.  

print("#################################################################")
print("#36. Check whether a variable is of type integer.")
print("#################################################################")


int_Num =123
print("Check type of variable:",type(int_Num))
print()


#37. Find the absolute value of a negative number.  
print("#################################################################")
print("#37. Find the absolute value of a negative number.")
print("#################################################################")

num = float(input("Enter a negative number: "))

absolute_value = abs(num)

print("Absolute value =", absolute_value)
print()


#38. Multiply two decimal numbers and print the result.  
print("#################################################################")
print("#38. Multiply two decimal numbers and print the result.")
print("#################################################################")

decimal1=123.2323
decimal2=1232.2323

print("Sum of two decimal numbers:",decimal1+decimal2)
print()

#39. Convert a decimal number into a string.  

print("#################################################################")
print("39. Convert a decimal number into a string.")
print("#################################################################")

decimal3 = 123.123213

print("covert decimal into string",str(decimal3))
print()


#40. Calculate the average of three numbers (including decimals). 
print("#################################################################")
print("#40. Calculate the average of three numbers (including decimals).")
print("#################################################################")

num1=10.0323
num2=10.32324
num3=30.43242

print(f"average of 3 numbers {num1},{num2},{num3}.Result:",(num1 + num2 + num3)/3)
print()


#SECTION 5: MIXED QUESTIONS  
#41. Create a simple calculator using basic operators.  
#42. Convert temperature from Celsius to Fahrenheit.  
#43. Check whether a number is positive, negative, or zero.  
#44. Find the sum of digits of a number.  
#45. Calculate the area of a circle using variables and float values.  
#46. Find the square and cube of a number.  
#47. Write a program to calculate the perimeter of a rectangle.  
#48. Take two decimal inputs and print their product.  
#49. Check if two numbers are equal using comparison operators. 
#50. Write a program to calculate the average of 5 user-input numbers. 

#41. Create a simple calculator using basic operators.  
print("#################################################################")
print("#41. Create a simple calculator using basic operators.")
print("#################################################################")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    print("Result =", num1 + num2)
elif choice == '2':
    print("Result =", num1 - num2)
elif choice == '3':
    print("Result =", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice!")

print()



#42. Convert temperature from Celsius to Fahrenheit.  
print("#################################################################")
print("#42. Convert temperature from Celsius to Fahrenheit.")
print("#################################################################")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)
print()



#43. Check whether a number is positive, negative, or zero.  

print("#################################################################")
print("43. Check whether a number is positive, negative, or zero.")
print("#################################################################")

Input_number=int(input("Please enter a number:"))

if Input_number > 0:
    print("Entered number is poistive:",Input_number)
elif Input_number < 0:
    print("Entered a number is Negative:",Input_number)
else:
    print("Entered number is zero: ",Input_number)
print()

#44. Find the sum of digits of a number.  
print("#################################################################")
print("#44. Find the sum of digits of a number.")
print("#################################################################")

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits =", sum_digits)
print()


#45. Calculate the area of a circle using variables and float values.  
print("#################################################################")
print("#45. Calculate the area of a circle using variables and float values.")
print("#################################################################")

radius = float(input("Enter the radius: "))
pi = 3.14159

area = pi * radius * radius

print("Area of the circle =", area)
print()

#46. Find the square and cube of a number.  
print("#################################################################")
print("#46. Find the square and cube of a number.")
print("#################################################################")
num=int(input("Please enter a number:"))

square= num ** 2
cube = num ** 3
print(f"The given number {num} square and cube is :",square , cube)

print()

#47. Write a program to calculate the perimeter of a rectangle.  
print("#################################################################")
print("47. Write a program to calculate the perimeter of a rectangle.")
print("#################################################################")

print("Formula of perimeter is: 2(l+w)")

length=int(input("Please enter length"))
width=int(input("Please enter width"))

print(f"Perimeter of rectangle is l is {length} and w is {width} ,perimeter is :",2(length+width))
print()

#48. Take two decimal inputs and print their product.  

print("#################################################################")
print("48. Take two decimal inputs and print their product.")
print("#################################################################")

d=2342.234
d1=2342.324

print(f"Two decimal value {d},{d1}:",d*d1)
print()

#49. Check if two numbers are equal using comparison operators. 
print("#################################################################")
print("49. Check if two numbers are equal using comparison operators.")
print("#################################################################")

a=int(input("please enter number:"))
b=int(input("please enter number:"))

if a == b:
    print(f"Both numbers{a},{b} are equal")
else:
    print(f"Both numbers {a},{b} are not equal")
print()


#50. Write a program to calculate the average of 5 user-input numbers. 
print("#################################################################")
print("50. Write a program to calculate the average of 5 user-input numbers.")
print("#################################################################")


num1=int(input("Please enter a number1:"))
num2=int(input("Please enter a number2:"))
num3=int(input("Please enter a number3:"))
num4=int(input("Please enter a number4:"))
num5=int(input("Please enter a number5:"))

print(f"Total average of 5 numbers {num1} , {num2} , {num3} , {num4} , {num5} average is:", (num1 + num2 + num3 + num4 + num5)/5 )
print()
