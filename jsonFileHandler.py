import json

def readJsonFileZauvik(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
            
    except IOError:
        print("Error file ga ada")
    return data
    
    
# insulinJson = readJsonFile("insulin.json")
# print(insulinJson)

