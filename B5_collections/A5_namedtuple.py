from collections import namedtuple
# Create a namedtuple called 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])
# Create an instance of the Point namedtuple
p1 = Point(10, 20)
# Access the fields of the namedtuple
print(p1.x)  # Output: 10
print(p1.y)  # Output: 20
# Create another instance of the Point namedtuple
p2 = Point(30, 40)
# Calculate the distance between p1 and p2
import math
distance = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
print(f"Distance between p1 and p2: {distance:.2f}")  # Output: Distance between p1 and p2: 28.28
# Create a namedtuple called 'Person' with fields 'name' and 'age'
Person = namedtuple('Person2', ['name', 'age'])
# Create an instance of the Person namedtuple   
person1 = Person("Alice", 30)
# Access the fields of the namedtuple
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
# Create another instance of the Person namedtuple
person2 = Person("Bob", 25)
# Calculate the age difference between person1 and person2
age_difference = abs(person1.age - person2.age)
print(f"Age difference between {person1.name} and {person2.name}: {age_difference} years") 
# Output: Age difference between Alice and Bob: 5 years


from collections import namedtuple

Employee = namedtuple("Employee", ["name", "role", "salary"], defaults=["Engineer", 0])

e = Employee("Alice")
print("e:", e)  # Employee(name='Alice', role='Engineer', salary=0)

# Convert to dict
print("e._asdict():",e._asdict())
