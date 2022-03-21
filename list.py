trainees = ["John", [2, ["Mary","J"]],38, 40.0]
# print 2
a=trainees[1]
c=a[0]
# print(c)

d=trainees[1][0]
# print(d)
#2. Output J using index, from the list.

j=trainees[1][1][1]

# print(j)

#3. Using a method add 56 at the end of the list.
trainees.append("56")

# print(trainees)

#4. Using a method add the name Mike between Mary and J
# trainees = ["John", [2, ["Mary","J"]],38, 40.0]

trainees[1][1].insert(1,'Mike')
print(trainees)




# #6. Remove John and ["Mary",”Mike”, "J"] 
# trainees.pop(0)
# trainees[0].pop(1)

# # print(trainees)

# # Using a function, determine the length of the list

# # d=trainees.__len__()
# # print(d)


# # Find the sum of the list

# # s=str(trainees)
# trainees[0]=trainees[0][0]
# # b=trainees[0][0]
# s = sum(trainees)
# print(s)