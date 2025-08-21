myList = ["Apple", "Grape", "Orange"]
for d in myList:
    print(d)
    
    
# Ideally "for-loop" is used for adding additional process before making an output
for i, d in enumerate(myList):
    print("{}. {}".format(i+1, d))
    

# Mixed data type
mixedTuple = ("Apple", 1, True, 5.55)
customIndex = 1
for d in mixedTuple:
    print("{}. Nyobain bikin output {}".format(customIndex, str(d)))
    # customIndex = customIndex+1
    customIndex += 1 # alternatif yang lebih keren dari customIndex = customIndex+1