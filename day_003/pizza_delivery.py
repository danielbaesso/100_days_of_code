print("Welcome to Python Pixxa Deliveries!")
size = input("What size pizza do you want? s, m or l: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")

bill = 0

# todo: work out how much they need to pay based on ther size choice.
if size == "s":
    bill += 15

if size == "m":
    bill += 20

if size == "l":
    bill += 25

else:
    print("Type a valid choice.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "n":
    pass

else:
    if size == "s":
        bill += 2

    if size == "m" or "l":
        bill += 3

    else:
        print("Type a valid choice.")

# todo: work out final amount based on wheter if they want extra cheese.
if extra_cheese == "y":
    bill += 1

if extra_cheese == "n":
    pass

else:
    print("Type a valid choice.")

print(f"Your order of pizza {size} is: ${bill}")
