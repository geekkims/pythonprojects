# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.
# Once you learn functions,revisit this and write this code inside a function.

# x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(x[:5])
# print(x[5:])


# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, display out a different message.
# Once you learn functions,revisit this and write this code inside a function.
number1 = input("Input Number")
number = int(number1)
if (number % 2) == 0 and (number %4) !=0:
    print("is even")
elif number % 4 == 0:
    print("Visible by 4")

else:
    print("is odd")


# Write a program that displays all prime numbers between 1 and 60.
# Hint: A prime number is a number that is divisible by ONLY 1 and itself.

# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
# h = input("Input h")
# i = input("Input I")
# j = input("Input J")

# if j < h > i:
#  print(h)

# elif j < i > h:
#     print(i)

# elif h < j > i:
#     print(j)


# Write a program that prompts the user to enter the base and height of a triangle and returns its area.

# h = float(input("Enter the height of the triangle"))
# b=float(input("Enter the base of the triangle"))
# a = h*b/2
# print("Area is: ", (a))

#     Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol.
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@” )


# email = input("Email Address: ")
# a = ("@" and "." in email)

# coneemail = "@" in email and "." in email

# print(coneemail)

# Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.

# print("Half Pyramid Pattern of Stars (*):")
# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print()