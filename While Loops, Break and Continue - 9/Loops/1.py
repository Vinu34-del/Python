# While Loop

is_failed = True
i = 1

while is_failed and i<=100:
    print(f"Try {i}")
    i = i + 1
print("I gave up!")

#break statement

for i in range(1,21):
    if i == 10:
        break
    print(i)

#continue statement
for i in range(1,12):
    if i == 3:
        continue
    print(i)