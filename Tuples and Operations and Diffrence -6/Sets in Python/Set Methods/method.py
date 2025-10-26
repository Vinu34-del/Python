s1 = {1,2,3}
s1.add(4)
print(s1)  # Output: {1, 2, 3, 4}

s1.remove(2)
print(s1)  # Output: {1, 3, 4}

s1.pop()
print(s1)  # Output: {3, 4} (or {1, 4} or {1, 3} depending on which element was popped)

s1.clear()
print(s1)  # Output: set()