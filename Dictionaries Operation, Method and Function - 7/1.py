#Dictionary
birthday = {
    "Vinay" : "4-july-2005",
    "Virat" : "5-nov-1988",
    "Rohit" : "30-april-1987"
}
print(birthday)

#Accessing Items
print(birthday["Virat"]) #Output: 5-nov-1988
print(birthday["Vinay"]) #Output: 4-july-2005
print(birthday["Rohit"]) #Output: 30-april-1987

#Adding Dictionary Items
birthday["Rana"] = "2-dec-1990" 
print(birthday)

# Updating Dictionary Items
birthday["Vinay"] = "3-dec-2000"
print(birthday)

#Removing Element
birthday.pop("Rohit")
print(birthday) #output: delete the rohit key value