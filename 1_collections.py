# # generic built-in functions
numbers = [45, 66, 12, 3, 99, 3.142, 42]
# min function, provides the smallest number in the list
# max function, provides the largest number in the list
print("min:", min(numbers), "max:", max(numbers))

# sum function adds all the numbers in the list together
print("sum:", sum(numbers))
print(f"Min: {min(numbers)} \tMax: {max(numbers)} \tSum: {sum(numbers)}")

# This helps separate the lines of code
print("\n" + "#" * 50)

names_lucky_numbers = {'fred': 3, 'jim': 8, 'dave': 42}

# min function returns the alphabetical minimum order of the keys, closer to A min, Z max
print("min:", min(names_lucky_numbers), "max:", max(names_lucky_numbers))
print(f"Min: {min(names_lucky_numbers)} Max: {max(names_lucky_numbers)}")
print("Dictionaries implement min, max and sum on the KEYS not the VALUES!")

print("\n" + "#" * 50)

# useful tuple operations
a = 'hello'
b = 'goodbye'
print(f"a: {a} \t b: {b}")

a, b = b, a

print(f"a: {a} \t b: {b}")

# range produces a sequence of 0 1 2 and stores it in the cheese variables
Gouda, Edam, Caithness = range(3)
print(Gouda, Edam, Caithness)
print(f'Gouda: {Gouda} \t Edam: {Edam} \t Caithness: {Caithness}')

# tuples don't need brackets!
mytuple = 'a', 'b', 'c'

# This is an example of operator overloading
another = mytuple * 4
print(another)

thing = ('Hello')
print(type(thing))

# It's the comma that makes the tuple! Nothing else
# Kind of question you we be asked in a coding interview
thing = 'Hello',
print(type(thing))

print("\n" + "#" * 50)
# Python Lists

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# subscript notation / index notation are the number in the brackets
print(cheese[1])
# minus numbers count from the right to the left
cheese[-1] = 'Red Leicester'
print(cheese)

print("\n" + "#" * 50)

# Tuple and List Slicing
mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
print(mytuple[2:4])
# ('spam', 'tea')

print(mytuple[-4])
# bacon
# list function is a constructor
mylist = list(mytuple)
# from index 1-til the end
print(mylist[1:])
# ['bacon', 'spam', 'tea', 'beans']
# From index 0-1
print(mylist[:2])
# ['eggs', 'bacon']


cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']
print("\n")
print(cheese)

# del is the delete statement
# You can slice a list to delete some items as well
del cheese[1:3]
print(cheese)

print("\n" + "#" * 50)

# Extended Iterable Unpacking

food_and_drink = 'eggs', 'bacon', 'spam', 'tea', 'coffee'
# too many values to unpack in x y z, need 4 variables
# x, y, z = food_and_drink

# * means scoop up everything leftover and store it in z, a list
*x, y, z = food_and_drink
print(f"x: {x} \t y:{y} \t z:{z}")

t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'

for a, *b, c in t1, t2:
    print(a, b, c)

print("\n" + "#" * 50)

# Adding Items to a List
#  on the left
print(cheese)

# Slicing the place in the cheese list and adding Chesthire and Ilchester
cheese[:0] = ['Cheshire', 'Ilchester']
print(cheese)

# on the right
# Appends these items to the end of the cheese list
cheese += ['Oke', 'Devon Blue']
print(cheese)

# extend method also appends to the end of the cheese list
# Without the square brackets, each character will be appended to the list
cheese.extend(['Oke', 'Devon Blue'])
print(cheese)

# append - one item only
cheese.append('Red Fox')
print(cheese)

# anywhere
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print("New cheese list:", cheese)
cheese.insert(2, 'Cornish Brie')
print(cheese)

# This is how to put it in a position between other items
cheese[2:2] = ['Dairy Lea Triangles']
print(cheese)
# Preferred and easier way to read how you are adding to a list
cheese.insert(0, 'Laughing Cow Triangles')
print(cheese)

print("\n" + "#" * 50)

# Removing items by position

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

# Pops out the Stilton, default without a number is popping the last item
saved = cheese.pop(1)
print("Saved1:", saved, ", Result:", cheese)

saved = cheese.pop()
print("Saved2:", saved, ", Result:", cheese)

print("\n" + "#" * 50)

# Removing items by content
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
print(cheese)
# remove method finds Oke, the first most Oke, and gets rid of it
cheese.remove('Oke')
print(cheese)

# raise exception, error happens when string doesn't exist
# cheese.remove('Brie')

print("\n" + "#" * 50)

# Sorting
# list.sort sorts the list in place. Lists are mutable.
cheese = ['Cornish Yarg', 'Oke', 'Edam', 'Stilton']
print(f"Cheese before sorting: {cheese}")

# sot() method sorted the list alphabetically
cheese.sort()
print(f"Cheese after sorting: {cheese}")

# sort key is a function, we can pass items into to use a function
# takes the length of each cheese word and sorts it by smallest to largest character numbers
cheese.sort(key=len)
print(f"Cheese after sorting by length: {cheese}")

# This is from the longest cheese names first to the shortest names
cheese.sort(key=len, reverse=True)
print(f"Cheese after sorting by length in reverse order: {cheese}")

# sorted is for ANY iterable
# it returns a list
hobby_tuple = 'Yoga', 'Pilates', 'Gardening', 'Baking', 'Rubiks Cubing'
print(hobby_tuple)

# sort method and sorted function are different!
# sorted method helps make it a list first and then, sort method can be used
hobby_list_sorted = sorted(hobby_tuple, reverse=True)
print(f"Hobbies sorted using the sorted function (becomes a LIST): {hobby_list_sorted}")

hobby_list_sorted = sorted(hobby_tuple, key=len)
print(f"Hobbies sorted using the sorted function by length: {hobby_list_sorted}")

print("\n" + "#" * 50)

# Miscellaneous List Methods
print(cheese)
edam_count = cheese.count('Edam')
print(f"Edam appears {edam_count} time(s).")

# index method checks the position of a string in a list
edam_index = cheese.index('Edam')
print(f"Edam appears at position {edam_index}.")

# reverse the list in place
print(f"Before reverse: {cheese}")
cheese.reverse()
print(f"After reverse: {cheese}")

print("\n" + "#" * 50)

# List Methods

# if cheese: checks if there are any items in the list
# Returns True if it is not empty and False if it is empty
if cheese:
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

# clear a list
cheese.clear()
if cheese:
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

print(cheese)