# 4. defaultdict – no more key errors
from collections import defaultdict 
# Create a defaultdict with a default factory of int (default value is 0)
dd = defaultdict(int)
# Accessing a non-existent key returns the default value (0)
print(dd["missing_key"])  # Output: 0
# Incrementing a non-existent key works without KeyError
dd["counter"] += 1
print(dd["counter"])  # Output: 1
# Create a defaultdict with a default factory of list (default value is an empty list)
dd_list = defaultdict(list)
# Accessing a non-existent key returns the default value (empty list)
print(dd_list["missing_key"])  # Output: []
# Append to a non-existent key works without KeyError
dd_list["my_list"].append(1)
dd_list["my_list"].append(2)
print(dd_list["my_list"])  # Output: [1, 2]
# Create a defaultdict with a default factory of str (default value is an empty string)
dd_str = defaultdict(str)
# Accessing a non-existent key returns the default value (empty string)
print(dd_str["missing_key"])  # Output: ''
# Concatenating to a non-existent key works without KeyError
dd_str["greeting"] += "Hello"
dd_str["greeting"] += " World"
print(dd_str["greeting"])  # Output: Hello World
# Create a defaultdict with a custom default factory
def default_value():
    return "default"
dd_custom = defaultdict(default_value)
print(dd_custom["missing_key"])  # Output: default

# Grouping data with defaultdict
students = [
    ("Alice", "Math"),
    ("Bob", "Math"),
    ("Alice", "Physics"),
]

by_student = defaultdict(list)

for name, subject in students:
    by_student[name].append(subject)

print(by_student)

# 7. Advanced patterns & real-world examples
# Frequency-based ranking system
from collections import Counter, defaultdict

logs = [
    ("alice", "login"),
    ("bob", "login"),
    ("alice", "upload"),
    ("alice", "login"),
]

user_actions = defaultdict(Counter)

for user, action in logs:
    user_actions[user][action] += 1

print("frequency based ranking system: ",user_actions["alice"])
print("frequency based ranking system: ",user_actions["bob"])
print("frequency based ranking system: ",user_actions["charlie"])  # charlie has no actions, but won't raise KeyError
print("frequency based ranking system: ",user_actions["alice"]["login"])  # charlie has no login actions, but won't raise KeyError
print("frequency based ranking system: ",user_actions["charlie"]["upload"])  # charlie has no upload actions, but won't raise KeyError
print("frequency based ranking system: ",user_actions)  # charlie has no download actions, but won't raise KeyError