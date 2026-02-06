# 1. Dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)

# 🔸 2. Zipping lists
names = ["a", "b", "c"]
ages = [18, 19, 20]

for name, age in zip(names, ages):
    print("Zipping:",name,"-", age)

# 🔸 3. Unpacking in loops
pairs = [(1,2), (3,4), (5,6)]

for x, y in pairs:
    print("Unpacking loops: ",x + y)