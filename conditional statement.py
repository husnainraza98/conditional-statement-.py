# 1. Write a program that checks if a given number is positive, negative, or zero.

number = int(input("Enter The Number : "))

if number > 0 :
    print("This Number is positive")
elif number < 0 :
    print("This Number is Negitive")
else :
    print("This Number is Zero") 

# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

user_age = int(input("Enter Your Age : "))

if user_age < 18:
    print("you are Minor person")
elif user_age < 64:
    print("you are Adult person")
else:
    print("You are a senior citizen.") 

# 3. Write a program that checks if a given year is a leap year.

year = int(input("Enter Year : "))

if year % 4 == 0 :
    print("This year is leap ")
else :
    print("This year is not leap year ") 

# 4. Take an integer and check if it’s even or odd.

number = int(input("Enter your number : "))

if number % 2 == 0 :
    print("This is Even Number")
else:
    print("This os Odd Number")

# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

input_number = int(input("Enter the your number Percentage : "))

if input_number > 90:
 print("A grade")
elif input_number > 80:
 print("B grade")
elif input_number > 70:
 print("C grade")
elif input_number > 60:
 print("C grade")
elif input_number > 50:
 print("D grade")
else :
 print("F grade")

 # 6. Write a program to find the largest of two numbers

number1 = int(input("Enter first number :"))
number2 = int(input("Enter second number :"))

if number1 > number2 :
    print(f"Largest number is {number1}")
else :
    print(f"Largest number is {number2}")

# 7. Write a program to find the largest of three numbers.
number1 = int(input("Enter first number :"))
number2 = int(input("Enter second number :"))
number3 = int(input("Enter third number :"))

if number1 > number2 and  number1 > number3:
    print(f"Largest number is {number1}")
elif number2 > number1 and  number2 > number3:
    print(f"Largest number is {number2}")
else :
    print(f"Largest number is {number3}")

    # 8. Create a program that checks if a given string is a palindrome

string = input("Enter Your String : ")

reversed_string = string[ ::-1]

if string == reversed_string :
    print("This string is palindrome")
else :
    print("This string is not palindrome")

    # 9. Take three sides of a ritangle as input and check if they form a valid triangle.

first_side = int(input("Enter Your first side :"))
second_side = int(input("Enter Your second side :"))
third_side = int(input("Enter Your third side :"))

if (first_side + second_side > third_side and
    first_side + third_side > second_side and
    second_side + third_side > first_side):
    print("This is valid triangle")
else:
    print("This is not valid triangle")

    # 10. Write a program to determine if a given character is a vowel or consonant.

character = input("Enter the character : ").lower()

if character in "aeiou":
    print("This Chraracter is vowel")
else:
    print("This Chraracter is consonant")

    # 11. Check if a given number is a multiple of both 3 and 5.

number = int(input("Enter the Number : "))

if number % 3 == 0 and number % 5 == 0:
    print("This number is multiple of both 3 and 5.")
else:
    print("This is not Multiple of 3 and 5")

    # 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot

temperature = int(input("Enter Temerature is celsius : "))


if temperature <= 0:
    print("Freezing")
elif 1 <= temperature <= 24:
    print("Moderate")
else:
    print("Hot")

    # 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding 

firstNumber = int(input("Enter your first Number : "))
secondNumber = int(input("Enter your second Number : "))
operator = input("Wich operator (+, -, *, /) you want to applay ? : ")

if operator == "+":
    print(firstNumber+secondNumber)
elif operator ==  "-":
    print(firstNumber-secondNumber)
elif operator == "*":
    print(firstNumber*secondNumber)
elif operator == "/":
    print(firstNumber/secondNumber)
else:
    print("Invalid operator")

    # 14. Check if a year input by the user is a century year.

year = int(input("Enter year : "))

if year % 100 == 0 :
    print("This is century year.")
else :
    print("This is not century year.")

    # 15. Write a program to check if a number is within a specified range.

number = int(input("Enter the Number : "))
range = int(input("Enter the ramge : "))

if number <= range :
    print("This number is in range")
else:
    print("This number is not in range")

    # 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

#  equilateral : a triangle that has all its sides equal in length
#  isosceles   : a triangle with (at least) two equal sides
#  scalene     : a triangle in which all three sides are in different lengths

first_side = int(input("Enter the first side of triangle : "))
second_side = int(input("Enter the second side of triangle : "))
third_side = int(input("Enter the third side of triangle : "))

if first_side + second_side > third_side and first_side + third_side > second_side and third_side + second_side > first_side :

    if first_side == second_side == third_side :
        print("This is equilateral triangle")
    elif first_side == second_side or second_side == third_side or first_side == third_side:
        print("This is isosceles triangle")
    else :
        print("This is scalene triangle")
else :
    # 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

number = int(input("Enter the Number : "))

if number % 2 == 0 and number % 3 == 0 :
    print("This Number is divisible by 2 and 3")
else:
    print("This is not divisible by 2 and 3")

    # 18. Take a user’s score and determine if they pass or fail (pass if 50 or above).

score = int(input("Enter your score : "))

if score >= 50 :
    print("pass")
else :
    print("fail")

    # 19. Check if a string input is uppercase, lowercase, or a mix.

string = input("Enter the string : ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

if string in upper :
    print("uppercase")
elif string in lower :
    print("lowercase")
else:
    print("uppercase and lowercase")

    # 20. Create a program that evaluates if an inputted number is prime.

number = int(input("Enter a number to check if it's prime: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False 
            break
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")