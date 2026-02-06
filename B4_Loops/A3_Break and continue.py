for i in range(10):
    if i == 5:
        break     # stops loop
    print(i)

print("Loop ended")
for i in range(5):
    if i == 2:
        continue  # skip this iteration
    print(i)