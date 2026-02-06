
from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = Counter(data)
print(counts)
print(counts["apple"])  # 3
print(counts["banana"])  # 2
print(counts["orange"])  # 1
# Most common elements
print(counts.most_common(2))  # [('apple', 3), ('banana', 2)]
# Update counts with new data
new_data = ["banana", "orange", "grape"]
counts.update(new_data)
print(counts)  # Counter({'apple': 3, 'banana': 3, 'orange': 2, 'grape': 1})
# Subtract counts
subtract_data = ["apple", "banana"]
counts.subtract(subtract_data)
print(counts)  # Counter({'apple': 2, 'banana': 2, 'orange': 2, 'grape': 1})
# Convert to a regular dictionary
counts_dict = dict(counts)  
print(counts_dict)  # {'apple': 2, 'banana': 2, 'orange': 2, 'grape': 1}    

a = Counter("aabbcc")
b = Counter("bccddd")

print("addition: ",a + b)   # addition
print("subtraction: ",a - b)   # subtraction
print("intersection: ",a & b)   # intersection
print("union: ",a | b)   # union


