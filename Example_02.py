# Create an Array in Python
import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

# Adding Elements to an Array
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

# Accessing Elements from the Array
print("Access element is: ", a[0])

# Removing Elements from the Array
a.remove(1)
print("The array after removing is : ", end="")
for i in (a):
    print(i, end=" ")