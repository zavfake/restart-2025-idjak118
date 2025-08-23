# List (Mutable -> Member value can be updated)
myList = ["Apple", "Grape", "Orange"]
print("==={}===".format(str(type(myList))))
print(myList) # Call all list members
print(myList[0]) # Call specific member using index
print(myList[0:2]) # Call list members within a range
print(myList[-2:]) # Call n list member from the last index
# modifying list
myList[0] = "Banana"
print("myNewList: {}".format(myList))

# Tuple (Immutable -> Member value is fixed)
myTuple = ("Apple", "Grape", "Orange")
print("==={}===".format(str(type(myTuple))))
print(myTuple) # Call all tuple members
print(myTuple[0]) # Call spesific member
print(myTuple[0:2]) # Call list members within a range
print(myTuple[-2:]) # Call n list member from the last index
# Modifying tuple
# myTuple[0] = "Banana" ERROR: 'tuple' object does not support item assignment
# print("myNewTuple: {}".format(myTuple))


# Dictionary (Mutable)
myDictionary = {
    "fruit1": "Apple",
    "fruit2": "Grape",
    "fruit3": "Orange",
}
print("==={}===".format(str(type(myDictionary))))
print(myDictionary)
print(myDictionary["fruit1"])

# Complex data structure. In real case, we combines both of them
myRecord = [
        {
            "name": "Zauvik",
            "address": "Solo"
        },
        {
            "name": "Chalila",
            "address":"Bekasi"
        }
    ]
    
print("==={}===".format(str(type(myRecord))))
print(myRecord[0]['name']) # Call nested value