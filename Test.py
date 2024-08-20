menu = "Latte, Black Coffee, Americano, Cappucino" #This is variable for menu

name = input("Hello!What is your name?\n") #Creating variable from user input

if name == "Janis":
    print("You are not wellcome here!!")
    exit()
else:
    print("Thank you " + name + " for comming to our CoffeeShop!\n")

#This is variable for order
order = input("Here is our menu:\n" + menu + "\n" + "What would you like to order?\n")

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


print("Sounds good "+ name + ", your " + order + " will be ready in a moment." + "Your bill is " + str(amount) + "€")
