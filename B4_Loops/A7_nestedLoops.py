for i in range(3):
    for j in range(2):
        print(i,j)


# super code.
# 9. List Comprehension (compact loops)
squares = [x*x for x in range(10)] # x*x  and x both are different.
print(squares)


# 10. Generator comprehensions
print("Generator comprehension:")
gen = (x*x for x in range(5))

for val in gen:
    print(val)

# 1. Dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)
