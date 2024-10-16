#For example, use the filter function () to refine even the even numbers from the list.

my_list = [1, 2, 4, 6, 8, 11, 3, 5]

new_list1 = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list1)

#For example, use the MAP () function to double all items in a list.
new_list2 = list(map(lambda x: x * 2 , my_list))

print(new_list2)
