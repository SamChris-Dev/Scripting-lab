# counter = 6
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# for i in range(2, 8):
#     print("The value of i is currently", i)

# for i in range(1, 1):
#     print("The value of i is currently", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# largest_number = -99999999
# counter = 0

# number = int(input("Enter a number or type -1 to end program: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end the program: "))

# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# i = 1
# while True:
#     if i == 3:
#         break
#     print(i, end=" ")
#     i += 1

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.

# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.

# numbers[0] = 111
# print("\nPrevious list contents:", numbers)  # Printing previous list contents.

# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list contents:", numbers)  # Printing current list contents.

# print("Hello")
# print("okay")
# print("People")

# numbers = [1,2,3,4,5,6,7,8,9,10]
# length = len(numbers)
# print("The length of the list is: ", length)
# print(numbers)

# del numbers[9]
# print("The length of the list is: ", len(numbers))
# print(numbers)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)

# list = [16,23,0,7,4,20,26]
# print("Before the bubble sort algorithm", list)
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(list) - 1):
#         if list[i] > list[i+1]:
#             swapped = True
#             list[i],list[i+1] = list[i+1],list[i]
#             print("During the swap", list)
# print("After the bubble sort algorithhm", list)           


# list = [2,3,1]
# print("Before the bubble sort algorithm", list)
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(list) - 1):
#         if list[i] > list[i+1]:
#             swapped = True
#             list[i],list[i+1] = list[i+1],list[i]
# print("After the bubble sort algorithhm", list)           

# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

# my_list = [1,2,4,4,1,4,2,6,2,9]

# for j in my_list:
#     sample = my_list[j]
#     for i in range(1+j, len(my_list)):
#         if sample == my_list[i]:
#             print(my_list[i])
#             # del new_list[i]

# print(new_list)

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# del list_1[0]
# del list_2

# print(list_3)


# my_list = [1, 2, "in", True, "ABC"]

# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False

# temps = [[0.0 for h in range(24)] for d in range(31)]

# print(temps)

# [  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  , [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#  ]


# A four-column/four-row table ‒ a two dimensional array (4x4)

# table = [[0,1,0,1],
#          [1,0,0,1],
#          [0,1,0,1],
#          [1,0,1,0]]

# print(table)
# print(table[0][0])  # output is zero 0
# print(table[0][3])  # output is one 1

# list = [8,5,4,3,6,7,8]
# list.sort()
# print(list)

# def intro(fname = "Samwel", lname = "Simule"):
#     print("Hello your name is" , fname , lname)

# intro("Sam","Chris")
# intro("Sam")
# intro()
# intro(lname = "Dooper")

# def add(a,c, b=1):
#     print(a+b+c)

# add(c=1,a=2)


# factorial 
#  0! = 1
#  1! = 1
#  2! = 1 * 2
#  3! = 1 * 2 * 3
#  4! = 1 * 2 * 3 * 4

# def factorial_func(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range(2, n+1):
#         product *= i
#     return product

# n = int(input("Enter a number: "))
# print("The ans is: ", factorial_func(n))


# def fibonacci(n):
#     if n < 3:
#         return 1
#     no1 =1
#     no2 = 1
#     sum = 0
#     for i in range (2,n):
#         sum = no1 + no2
#         no1 = no2
#         no2 = sum
#     return sum

# n = int(input("Please enter your number: "))
# print("Since n=",n ,"Then the answer is:", fibonacci(n))


# def fib(n):
#     if n < 3:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input("Please enter your number: "))
# print(fib(n))

# list = ["Samwel","google",6,7,8,3,5,1,1.0]
# print(list)

# my_tuple = (1, 10, 100, 1000)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10

# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1 = t3 
# t2 = t1
# t3 = t2

# print(t1, t2, t3)


# var2 = 123

# t10 = (1, )
# t20 = (2, )
# t30 = (3, var)

# t10, t20, t30 = t30, t10, t20
# print(t10, t20, t30)


# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# for key in dictionary.values():
#     print(key, "->", values)

# print("\n")
# for key, item in dictionary.items():
#     print(key, "->", item)


# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break

#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

