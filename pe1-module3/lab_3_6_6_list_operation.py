my_list = [1,2,4,4,1,4,2,6,2,9]

new_list = []

for num in my_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)



# print(new_list)




# for j in range(len(my_list)):
#     sample = my_list[0]
#     for i in range(len(my_list)-1):
#         if sample == my_list[i+1]:
#             print(my_list[i+1])

# print(new_list)

# sample = my_list[0]
# for i in range(1, len(my_list)-1):
#     if sample == my_list[i]:
#         print(my_list[i])
#         del new_list[i]

# print(new_list)

# for j in range(len(my_list)):
#     sample = my_list[j]
#     for i in range(1+j, len(my_list)):
#         if sample == my_list[i]:
#             print(my_list[i])
#             # del new_list[i]

# print(new_list)