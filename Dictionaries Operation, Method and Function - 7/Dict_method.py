birthday = {
    "Vinay" : "4-july-2005",
    "Virat" : "5-nov-1988",
    "Rohit" : "30-april-1987"
}
print(birthday)

#Dict Methods
#Keys():Returns all the keys in the Dictionary

print(birthday.keys())

# Values: Return all the values in the Dictionary

print(birthday.values())

#items: Returns key-value pairs tuples

print(birthday.items())

#update: Updates the Dictionary
dict2 = {"Vikas" : "3-july-2005"}
birthday.update(dict2)
print(birthday)
