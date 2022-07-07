# # # Exercise 1: Create a list by picking  odd-index items from the first list and even index items from the second
# # # Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
# #
# # l1 = [1, 2, 3, 4, 5, 6]
# # l2 = [7, 8, 9, 10, 11]
# #
# # # odd l1 = 2[1], 4[3], 6[5]
# # #even l2 = 7[0], 9[2], 11[4]
# #
# # l3 = l1[1:6:2] + l2[0:5:2]
# # print(l3)
# #
# # #sau
# #
# # odd_elements = l1[1::2]  # toate lista, de la index 1, din 2 in 2 - nu puntem finalul
# # even_elements = l2[0::2]
# #
# # l4 = list()
# #
# # l4.extend(odd_elements)
# # l4.extend(even_elements)
# # print(l4)
#
#
# #Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
#
# # list = []
# # for i in range(9,51):
# #     if i % 2 == 0:
# #        list.append(i)
# # print(list)
#
# # Reverse a list in Python
#
# # list1 = [100, 200, 300, 400, 500]
# # list1.reverse()
# # print(list1)
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# list3 = [i + j for i, j in zip(list1,list2)]
# print(list3)
#
# #Turn every item of a list into its square
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#     res.append(i * i)
# print(res)
#
# #or
#
# res2 = [x * x for x in numbers]
# print(res2)


# #1. Write a Python program to sum all the items in a list.
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma = 0
#
# for i in lista:
#     suma += i
#
# print(suma)

# # 2. Write a Python program to multiply all the items in a list.
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma = 1
#
# for i in lista:
#     suma *= i
#
# print(suma)


# #1. Write a Python script to sort (ascending and descending) a dictionary by value
#
# import operator
# dictionar = {1:10,  3:30, 2:20, 5:50, 4:40, 6:60, 7:70}
# sorted_dict = sorted(dictionar.items(), key=operator.itemgetter(1))
# reverse_dict = dict(sorted(dictionar.items(), key=operator.itemgetter(1), reverse=True))
# print(f'Dict original: {dictionar}, Dict ascendent: {sorted_dict}, dict descendent: {reverse_dict}')

# #2. Write a Python script to add a key to a dictionary.
#
# sample = {0: 10, 1: 20}
# sample.update({2:30})
# print(sample)

#
# #3. Write a Python script to concatenate following dictionaries to create a new one.
#
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
#
# for d in (dic1,dic2,dic3):
#     dic4.update(d)
# print(dic4)
#
# # Take a list, say for example this one:
# #
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
#
# for number in a:
#     if number < 5:
#         print(number)
#
# b = []
#
# for number in a:
#     if number < 5:
#         b.append(number)
# print(b)
#
# nr = int(input('Numar ales: '))
#
# for number in a:
#     if number < nr:
#         b.append(number)
# print(b)

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

# x = int(input('Introduceti un numar: '))
#
# if x % 4 == 0:
#     print(f'Nr {x} este multiplu de 4')
# elif x % 2 == 0:
#     print(f'Nr {x} este un nr par')
# else:
#     print(f'Nr {x} este un nr impar')
#
#
# num = int(input('Nr 1: '))
# check = int(input('Nr 2: '))
#
# if check & num == 0:
#     print(f'Nr {check} se imparte exact la {num}')
# else:
#     print(f'{check} nu se imparte exact la {num}')


# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
#
# for x in a:
#     if x in b and x not in c:
#         c.append(x)
# print(c)
#
# #sau
#
# d = set(a).intersection(set(b))
# print(list(d))
#
# import random
#
# lst1 = random.sample(range(100), k=10)
# print(lst1)
#
# lst2 = random.sample(range(100), k=15)
# print(lst2)
#
# lst3 = set(lst1).intersection(set(lst2)) # transformam lista 1 in set, facem intersectia cu set din lista 2
# print(list(lst3)) # transformam setul de mai sus inapoi in lista

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# #
# # a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # b = [x for x in a if x % 2 == 0]
# # print(b)
#
# # Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# # makes a new list of only the first and last elements of the given list.
#
#
# # a = [5, 10, 15, 20, 25]
# # b = [a[0],a[len(a)-1]]
# # print(b)
#
# # Exercise 1: Reverse a list in Python
#
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
#
# print(list1)
#
# #sau cu slicing
# list1 = list1[::-1]
# print(list1)
#
# #Concatenate two lists index-wise
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# list3 = [i + j for i, j in zip(list1,list2)] # This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
# print(list3)
#
# list3 = [1, 2, 3, 4, 5, 6]
# list4 = [9, 8, 7, 6, 5]
#
# list5 = [i + j for i, j in zip(list3, list4)]
# print(list5)
#
# #Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squares = []
#
# for i in numbers:
#    squares.append(i*i)
# print(squares)
#
# #sau
# squares2 = [i * i for i in numbers]
# print(squares2)
#
# #Concatenate two lists in the following order ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# res = [x + y for x in list1 for y in list2]
# print(res)
#
# # Iterate both lists simultaneously
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# for x, y in zip(list1, list2[::-1]):
#     print(x,y)
#
# #Remove empty strings from the list of strings
#
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
# res = list(filter(None,list1)) # filtram valorile None
# print(res)

#Write a program to add item 7000 after 6000 in the following Python List: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#indexes
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[2][1])
print(list1[2][0])
print(list1[2][2])
print(list1[3])

list1[2][2].append(7000)
print(list1)
