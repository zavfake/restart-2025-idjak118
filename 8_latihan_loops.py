import random

number = random.randint(1,10)
print("contekan {}".format(str(number)))
restart = True
    
# while restart == True: # Selalu jalankan kode di dalam while ketika nilai restart sama dengan True
#     yourNumber = input("Guess the number ")
#     if(int(yourNumber) == number):
#         print("You are WIN!")
#         restart = False # Pemberian nilai baru, prevent restart ketika game menang
#     else:
#         print("Ohh man, pls try again!")

print("Looping dictionary")
myDict = {
    "nama": "Zauvik",
    "address":"Solo"
}  
# looping by using keys accessor
for key in myDict.keys():
    print("{} : {}".format(key, myDict[key]))
    
# looping using value-key pair
for key, d in myDict.items():
    print(key, d)
    
# looping using value only
for v in myDict.values():
    print(v)


# creating loop using range of value
for d in range(1,10000):
    print(d)