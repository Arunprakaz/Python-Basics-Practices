from collections import deque
# Create a deque with some initial elements
d = deque(['a', 'b', 'c'])
print("Initial deque:", d)  # Output: Initial deque: deque(['a', 'b', 'c'])
# Append elements to the right end      
d.append('d')
print("After appending 'd':", d)  # Output: After appending 'd': deque(['a', 'b', 'c', 'd'])
# Append elements to the left end   
d.appendleft('z')
print("After appending 'z' to the left:", d)  # Output: After appending 'z' to the left: deque(['z', 'a', 'b', 'c', 'd'])
# Pop elements from the right end
right_pop = d.pop() 
print("Popped from the right:", right_pop)  # Output: Popped from the right: d
print("Deque after popping from the right:", d)  # Output: Deque after popping from the right: deque(['z', 'a', 'b', 'c'])
# Pop elements from the left end    
left_pop = d.popleft()
print("Popped from the left:", left_pop)  # Output: Popped from the left: z
print("Deque after popping from the left:", d)  # Output: Deque after popping from the left: deque(['a', 'b', 'c'])
# Extend the deque on the right end     
d.extend(['e', 'f'])
print("After extending on the right:", d)  # Output: After extending on the right: deque(['a', 'b', 'c', 'e', 'f'])
# Extend the deque on the left end
d.extendleft(['x', 'y'])
print("After extending on the left:", d)  # Output: After extending on the left: deque(['y', 'x', 'a', 'b', 'c', 'e', 'f']) 
# Rotate the deque to the right by 2 steps
d.rotate(2) 
print("After rotating to the right by 2 steps:", d)  # Output: After rotating to the right by 2 steps: deque(['e', 'f', 'y', 'x', 'a', 'b', 'c'])
# Rotate the deque to the left by 3 steps       
d.rotate(-3)
print("After rotating to the left by 3 steps:", d)  # Output: After rotating to the left by 3 steps: deque(['x', 'a', 'b', 'c', 'e', 'f', 'y']) 
# Clear the deque
d.clear()
print("After clearing the deque:", d)  # Output: After clearing the deque: deque([])   

# Fixed-length deque (sliding window)
# dq=[(1,2,3)]
dq = deque(maxlen=3)

for i in range(5):
    dq.append(i)
    print(dq)
