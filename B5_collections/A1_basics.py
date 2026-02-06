# 1. List
numbers = [1, 2, 3, 4]
# 📌 Mutable and ordered.

print(numbers.append(5))
print(numbers.pop()) #// display last index value and remove it from list
print(numbers.clear())
print(numbers)


# 📌 2. Tuple
coords = (10, 20)


# 📌 Immutable, ordered.

# 📌 3. Set
colors = {"red", "green", "blue"}


# 📌 Unordered, unique values.

# 📌 4. Dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, value)

if "name" in person:
    print("Exists")





# 📌 Key → value mapping.

# In Python, mutable and immutable refer to whether an object’s value can be changed after it is created.

# 1. Mutable Objects
# Definition: Objects whose contents (value/state) can be changed after creation.
# Examples:
# list
# dict
# set
# bytearray
# Custom classes (by default, if attributes can be reassigned)
# Example:

# Python

# Copy code
# # Mutable example with list
# numbers = [1, 2, 3]
# numbers[0] = 10  # Modifies the existing object
# print(numbers)   # Output: [10, 2, 3]
# Here, the same list object is modified in place.

# 2. Immutable Objects
# Definition: Objects whose contents cannot be changed after creation.
# Any "change" creates a new object in memory.

# Examples:
# int
# float
# str
# tuple
# frozenset
# bytes

# Example:

# Python

# Copy code
# # Immutable example with string
# name = "Python"
# name = name.replace("P", "J")  # Creates a new string object
# print(name)  # Output: "Jython"
# Here, "Python" is not modified — instead, a new string "Jython" is created.