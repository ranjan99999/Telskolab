string = "hello how are you"
print(string)

my_list = [2, 1, 3, 5, 3, 9, 8, 5, 73, 2, 6]
for i in range(0, len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] >= my_list[j]:
         my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
