# if Statement
signal = "Red"
if signal == "Red":
    print("Stop")

# else Statement
signal = "Green" 
if signal == "Red":
    print("Stop")
else:
    print("Go") 

# elif Statement
signal = "Yellow"
if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Ready")
else:
    print("Go")


# Nested if Statement
gender = input("Enter your Gender: ")
age = int(input("Enter your age: "))

if gender == "Female":
    print("Ticket is free")
else:
    if age<5:
        print("You are child,low price")
    elif age >12:
        print("You are adult,full price")
    elif age >= 60:
        print("You are senior citizen,discount price")
    else:
        print("You are youth,medium price")