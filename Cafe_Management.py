print("***** PYTHON CAFE ****")
user_greetings=input("Input Your Name : ")
print(f"Hello, {user_greetings} Welcome to the cafe. ")
print(" *** Our Menu ***")
print(" Pizza: 450\n Burger: 300\n Momo: 130\n Sukuti: 200\n Milkshake: 100")
total_order=0
menu = {
    "pizza": 450,
    "burger": 300,
    "momo": 130,
    "sukuti": 200,
    "milkshake": 100
}
user_input = input("Input Your Order please : ").strip().lower()
if user_input in menu:
    total_order += menu[user_input]
    print(f"Your Order has been placed.")
else:
    print(f"Sorry, {user_input} is not a valid order.")
another_order=input("Would you like to order again?(Yes/No):- ").strip().lower()
if another_order == "yes":
    second_order=input("Enter Your Order please : ").strip().lower()
    if second_order in menu:
        total_order += menu[second_order]
        print(f"Your Order has been placed.")
print("Your Total Order Bill is NPR:",total_order)