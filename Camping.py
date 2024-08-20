
#Camping item list in variable
camping_list = ["tent", "sleeping bag", "shoes", "flashlight", "water bottle", "water", "milk", "food"]

#List with different data types
camp_site = ["Līgatne", 404, 24.50, True]

#Prints data type
print("Camping_list is of type", type(camping_list))

#Prints data type
print("camp_site is of type", type(camp_site))

#Append - adds one item to list
camping_list.append("toilet paper"), camping_list.append("towel")

#Extend - adds multiple items to list
camping_list.extend(["hat", "gloves"])

#+ - adds multiple items to list
camping_list = camping_list + ["kitchenware", "pots"]

#Insert - adds item to specified index (0 first, -1 last)
camping_list.insert(0, "sunglasses"), camping_list.insert(-1, "umbrella")


camping_list.remove("tent"), camping_list.remove("sleeping bag")

#Pops - removes item from specified index and returns it with print command
print(camping_list.pop(0))

#Prints list
print(camping_list)

#[0] - first item in a list
me = camping_list[0]

 #[1] - second item in a list
you = camping_list[1]

print("I will bring " + me + " and " + "you will bring " + you)