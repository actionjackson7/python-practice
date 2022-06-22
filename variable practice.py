#variable practice
#build a robot barista

print("Hello! welcome to the cafe!")
name = input("May I get your name? (Enter your name) : ")

#robo bouncer
if name == "Ben":
    evil_status = input("are you evil? ")
    if evil_status == "yes":
        print("gtfo rn bruh")
        exit()
    else:
        print("You're a good Ben! Come in!")
else:
    print("Hello " + name + " how are you today and what can I get you?")


#menu
menu = "Coffee\nCappuchino\nLatte\nBoba"

print("Here's our menu! \n" + menu)

#order here
order = input("Place your order here: ")

if order == "Boba":
    price = 13 
elif order == "Coffee":
    price = 5
elif order == "Latte":
    price = 8
elif order == "Cappuchino":
    price = 9
else:
    print("Sorry, we dont have that here.")


#quantity of item
how_many = input("How many would youy like? (numerical values only): ")

#calculate total
print("Thank you " + name + ". "+ "Your " + how_many + " " + order + " Will be ready soon")

total = price * int(how_many)

print("your total is " + "$" + str(total))





















