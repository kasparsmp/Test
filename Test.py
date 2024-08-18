menu = "Latte, Black Coffee, Americano, Cappucino" #This is variable for menu

print("Hello!")
customer = input("What is your name?\n") #Creating variable from user input

print("Thank you " + customer + " for comming to our CoffeeShop!\n")

order = input("Here is our menu:\n" + menu + "\n" + "What would you like to order?\n")

#order = input()

print("Sounds good "+ customer + ", your " + order + " will be ready in a moment.")