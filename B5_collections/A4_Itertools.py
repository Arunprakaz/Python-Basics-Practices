import itertools

# 1. Infinite counting
print("Infinite counting:") 
for i in itertools.count(1):
    if i > 5:
        break
    print(i)

# 2. Cycling through a list
print("\nCycling through a list:")
colors = ["red", "green", "blue"]
for color in itertools.cycle(colors):
    print(color)
    if color == "green":
        break

# 3. Repeating a value
print("\nRepeating a value:")
for val in itertools.repeat("Hello", 3):
    print(val)

# 4. Permutations   
print("\nPermutations of [1,2,3]:")
for perm in itertools.permutations([1,2,3]):
    print(perm)

# 5. Combinations
print("\nCombinations of [1,2,3] taking 2:")
for combo in itertools.combinations([1,2,3], 2):
    print(combo)

# 6. Product (Cartesian product)
print("\nCartesian product of [1,2] and ['a','b']:")
for prod in itertools.product([1,2], ['a','b']):
    print(prod) 
    
# combinations method
print("\nCombinations of [1,2,3] taking 2:")
for combo in itertools.combinations([1,2,3,4,5], 2):
    print(combo)


