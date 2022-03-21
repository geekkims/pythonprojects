# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that has an array or a list(only in python)  a = [5, 10, 15, 20, 25]. 
# Make a new array/list of only the first and last elements of the given array/list above. 
# Once you learn functions,revisit this and write this code inside a function.

# a = [5, 10, 15, 20, 25]
# b=a[0],a[4]
# print(b)

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, display out a different message.
# Once you learn functions,revisit this and write this code inside a function.

# a=input("Input Number")
# number=int(a)
# if (number%2)==0 and (number%4)!=0:
#     print("number is even")
# elif number%4==0:
#     print("number is divisible by four")
# else:
#     print("number is odd")


# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.





# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@” )
# Once you learn functions,revisit this and write this code inside a function.

# email=input("Input Email Address")
# a=("@" and "." in email)
# conemail="@" in email and "." in email
# print(conemail)


# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

# h=input("input h")
# j=input("Input J")
# i=input("Input I")

# if j<h>i:
#     print(h)
# elif h<j>i:
#     print(j)
# elif h<i>j:
#     print(i)


# TASK 6:Using Python Only
# Put number 1 till 50 in a tuple then,  print the first half values in one line and the last half values in another line.
# Once you learn functions,revisit this and write this code inside a function.

# a=(1,2,3,4,5,6,7,8,9,10)
# b=a[:5]
# c=a[5:]
# print(b)
# print(c)


# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that displays all prime numbers between 1 and 6,000.
# Hint: A prime number is a number that is divisible by ONLY 1 and itself.
# Once you learn functions,revisit this and write this code inside a function.

# for J in range(1,6001):
#     count=0
#     for i in range(2,(J//2+1)):
#         if(J%i==0):
#             count=count+1
#         break

#     if(count==0 and J !=1):
#         print("%d" %J,end=' ')


# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.

mark=int(input("Input marks: "))
if mark>100:
    print("Marks are Incorrect")
elif  mark>=79:
    print("Grade is A")
elif mark>=60:
    print("Grade is B")
elif mark>=49:
    print("Grade is C")
elif mark>=40:
    print("Grade is D")
elif mark<40:
    print("Grade is E")

# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the age in years and returns the age in days.Use 365 days as the length of a year for this challenge as we would like to ignore leap years. Only accept positive numbers.
# Once you learn functions,revisit this and write this code inside a function.





# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.

# height=float(input("Input the height of the triangle: "))
# base=float(input("Input the height of the triangle: "))
# area=height*base/2
# print(area)


# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.

# speed=int(input('Write the speed in km/h: '))
# deducted_points=(speed-70)/5


# if speed <70:
#     print('Ok')
# elif deducted_points>12:
#     print("Licence Suspended")
# else:
#     print("Deducted points:",deducted_points)





# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.
# Once you learn functions,revisit this and write this code inside a function.
# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print()
# rows=input("input the ")
# for i in range(rows):
#     print("*"*i)


# TASK 13: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [['omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
# omo=prods[0]
# omobal=int(omo[2])
# # print(omobal)
# milk=prods[1]
# milkbal=int(milk[2])
# # print(milkbal)
# bread=prods[2]
# breadbal=int(bread[2])
# # print(breadbal)
# coffee=prods[3 ]
# coffeebal=int(coffee[2])
# # print(coffeebal)

# a=omobal+milkbal+breadbal+coffeebal

# print(a)

# if i in prods:
#     print(i)




# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes 3 details (name,email and phone number) from a user as input, and stores them in one array/list then validates:
# i) if the email is valid
# ii) convert the phone to start from +254712345678 and
# iii) check if the name does not contain a number 
# If all these pass, print out the details in one list else display an error message.
# Once you learn functions,revisit this and write this code inside a function.

# name = input("Enter your name : ")

# if "1" in name or "2" in name or "3" in name or "4" in name or "5" in name or "6" in name or "7" in name or "8" in name or "9" in name  or "0" in name:

#     print("Oops..incorrect")

# else:

#     print("Looks good.")

# email = input("Good,now enter your email adress : ")

# if "@" in email  and "." in email and len(email)>=7:

#     print("Correct email adress, lets proceed")

# else:

#     print("Recheck your email adress")

 

# phone = list(input("Enter your phone number : "))

# if phone[0] == "0" and phone[1] == "7" and len(phone)==10:

#     del phone[0]

#     phone.insert(0, "+"), phone.insert(1, "2"),phone.insert(2, "5"), phone.insert(3,"4")

#     formatted1 = ''.join(phone)

#     print(formatted1)

# elif phone[0] == "0" and phone[1] =="1" and len(phone)==10 :

#     del phone[0]

#     phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")

#     formatted2 = ''.join(phone)

#     print(formatted2)

# elif phone[0] == "7" and len(phone)==9:

#     phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")

#     formatted3 =''.join(phone)

#     print(formatted3)

# elif phone[0] == "2" and phone[1] =="5" and phone[2] == "4" and len(phone)==12:

#     phone.insert(0,"+")

#     formatted4 = "".join(phone)

#     print(formatted4)

# elif phone[0] == "+" and phone[1] == "2" and phone[2] == "5" and phone[3] =="4" and len(phone) ==13:

#     formatted5 ="".join(phone)

#     print(formatted5)

# print(name,"you entered the following details")

# print("Your name : ",name)

# print("Your email : " ,email)

# print("Phone number  : ",''.join(phone))


# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.


# h = input("Input h: ")
# i = input("Input I: ")
# j = input("Input J: ")
# k=input("input i: ")

# if i<h and j<h and k<h:
#     print(h)
# elif h<i and j<i and k<i:
#     print(i)
# if i<j and h<j and k<j:
#     print(j)
# if j<k and h<k and i<k:
#     print(k)
# else:
#     print("Two or more numbers are equal")

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then return user “Login is Successful” and ONLY accepts 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.


# count=0
# while count<4:
#     email=input("Enter your Email Address: ")
#     Password=input("Enter Password: ")

#     if email=="admin@mail.com" and Password=="Admin@123":
#         print("Login Successful")
#         break
#     else:
#      print("Invalid Login")
#     if count==3:
#         print("Your Login has been blocked")
#     count +=1


# TASK 17: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.



print(r'foo\\bar\nbaz')