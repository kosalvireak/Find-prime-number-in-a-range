
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004,
#     "fav gift": online_store["keychain"],
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

#x = myfamily["child1"]["fav gift"]

online_store = {
    "keychain": 0.75,
    "t_shirt": 8.5,
    "bottle": 10
}
keychain = online_store["keychain"]
t_shirt = online_store["t_shirt"]
bottle = online_store["bottle"]
# NumOfKey = int(input("Enter number of keychain: "))
# NumOfShirt = int(input("Enter number of t-shirt: "))
# NumOfBottle = int(input("Enter number of bottle: "))
NumOfKey = 12
NumOfShirt = 13
NumOfBottle = 2
print("You have purchase "+str(NumOfKey)+" keychain, " +
      str(NumOfShirt)+" t-shirt, "+str(NumOfBottle)+" water bottle")
# if purchase more than 10 decrease price by 10%
# me = online_store["bottle"] = 2
# print(online_store["bottle"])


def function(key, keyname):
    name = "new" + str(key)
    if key > 10:
        name = keyname*0.9
    else:
        name = keyname
    print("New price of " + str(key) + " is: "+str(name))


function(NumOfKey, keychain)
function(NumOfShirt, t_shirt)
function(NumOfBottle, bottle)
