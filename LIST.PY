# list of integers
my_list = [1, 2, 3]



# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]



# nested list
my_list = ["mouse", [8, 4, 6], ['a']]


#Access List Elements
# List indexing

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o

print(my_list[4]) # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])




# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])


#Slicing Lists

# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# includes element at index 2, 3, 4
# excludes element at index 5
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])



#Add/Change List Elements
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd)             






# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)





# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)




# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
print(my_list)





my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)




# CHEETSHEET :

# Methods	Descriptions
# append()	adds an element to the end of the list
# extend()	adds all elements of a list to another list
# insert()	inserts an item at the defined index
# remove()	removes an item from the list
# pop()	    returns and removes an element at the given index
# clear()	removes all items from the list
# index()	returns the index of the first matched item
# count()	returns the count of the number of items passed as an argument
# sort()	sort items in a list in ascending order

