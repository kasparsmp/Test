menu = "Latte, Black Coffee, Americano, Cappucino" #This is variable for menu
price = 5 #This is variable for price (all menu items have the same price)


print("Hello!")
customer = input("What is your name?\n") #Creating variable from user input

print("Thank you " + customer + " for comming to our CoffeeShop!\n")

order = input("Here is our menu:\n" + menu + "\n" + "What would you like to order?\n")

cups = input("How many cups would you like?\n")
amount = price * int(cups) #This is variable for amount

print("Sounds good "+ customer + ", your " + order + " will be ready in a moment." + "Your bill is " + str(amount) + "€")
