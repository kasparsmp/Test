menu = "Latte, Black Coffee, Americano, Cappucino" #This is variable for menu

#Create variable for name
name = input("Hello! What is your name?\n")

#This is variable for name, and check if it is Janis or Juris, and  check if they are evil
if name == "Janis" or name == "Juris" or name == "Loki":
    status = input("You are evil?\n")
    deeds = int(input("How many evil deeds do you do today?\n"))
    if status == "yes" and deeds >= 4:
        print(name + " you did " + str(deeds) + " deeds" + ", you are not wellcome here!!")
        exit()
else:
    print("Thank you " + name + " for comming to our CoffeeShop!\n")

#This is variable for order
order = input("Here is our menu:\n" + menu + "\n" + "What would you like to order?\n")

#This is variable for price and check if milk is needed for Latte. If milk is needed, price is increased.
#If user writes item that is not in menu, program will exit.
if order == "Latte":
    milk = input("Would you like extra milk for your Latte?\n")
    if milk == "yes":
        price = 9
    else:
        price = 8
elif order == "Black Coffee":
    price = 4
elif order == "Americano":
    price = 3
elif order == "Cappucino":
    price = 5
else:
    print("Sorry we don't have that item")
    exit()

#This is variable for cups
cups = input("How many cups would you like?\n")

#This is variable for amount
amount = price * int(cups)

#Prints out text with confiramtion of order and payment amount
print("Sounds good "+ name + ", your " + order + " will be ready in a moment." + "Your bill is " + str(amount) + "€")
