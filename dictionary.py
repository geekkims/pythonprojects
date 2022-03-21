# person={"name":["Jay","Kim"],"Location":"Mombasa","Age":"20"}


# # Replace Jay with James


# person["name"]="James"
# n=person["name"]
# print(n)

# p= {"name":{"numero":[89,56,["",{"age":(30)}]]},"location":"Mombasa","age":"25"}

# print(p["name"]["numero"][2][1]["age"])


tasklist = [23, "Jane", ["Lesson 23", 560, {
    "currency": "KES"}], 987, (76, "John")]

# Determining type of variable taskList is, using an inbuilt function

# print(type(tasklist))

# Print KES

print(tasklist[2][2]["currency"])

# Print 560

print(tasklist[2][1])


# Use a function to determine the length of taskList

# print(tasklist.__len__())

# Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually
y = "12345"
# print(y[::-2])


# Change the name “John” to “Jane” .
# tasklist = [23,"Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]

d = list(tasklist[4])
d[1] = "Jane"
t = tuple(d)
tasklist[4] = t
# print(tasklist)

# 7. In the dictionary with the key currency, add another key “amount” with value 90

tasklist[2][2]["amount"]=90


# print(tasklist)
