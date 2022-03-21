# number = 45
# if number <= 15:
#     print("its less then 15")

# elif number > 10 and number <50:
#     print("number is gretaer than 10 and less than 20")
# else:
#     print("number is big")

# var = "Mark is here"
# if var.count("John") > 0:
#     print("John is in the sentence")
# elif var.count("Mark"):
#     print("Mark is in the sentence")
# elif var.count("Amina"):
#     print("Amina is here")


# Prompt the user to input the marks.
# The input should be between 0 and 100.
# Then output the correct grade:
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


# grade1= input("Number:  ")
# grade=int(grade1)
# if grade > 79:
#     print("A")
# elif grade >= 60 and grade <79:
#     print("B")
# elif grade >=49 and grade <59:
#     print("C")
# elif grade >=40 and grade <49:
#     print("D")
# elif grade <40:
#     print("E")
# Write a program that has an array or a list(only in python)  a = [5, 10, 15, 20, 25].
# Make a new array/list of only the first and last elements of the given array/list above.

# a = [5, 10, 15, 20, 25]
# b = [a[0],a[-1]]
# print(b)

# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# number1 = input("Input Number")
# number = int(number1)
# if number % 2 == 0 and number %4 !=0:
#     print("is even")
# elif number % 4 == 0:
#     print("Visible by 4")

# else:
#     print("is odd")

#   If the number is a multiple of 4, display out a different message.


# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254…
# e.g if a user enters “0712345678”, the program should display “+254712345678”

# number2 =input("Input Phone Number: ")

# if number2[0]=="7" and len(number2)==10:
   
# elif number2[0]=="0" and "number2[1]"




#     Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol.
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@” )


# email = input("Email Address: ")
# a = ("@" and "." in email)

# coneemail = "@" in email and "." in email

# print(coneemail)


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


# Write a program that displays all prime numbers between 1 and 60,000.
# Hint: A prime number is a number that is divisible by ONLY 1 and itself.
# Once you learn functions,revisit this and write this code inside a function.

for J in range(1,600001):
    count=0
    for i in range(2,(J//2+1)):
        if(J %i==0):
            count=count+1
            break

    if(count==0 and J !=1):
        print("%d" %J, end=' ')
