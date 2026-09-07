name = input("What is you name?: ")

print(f'Welcome, {name} to the Launch Console!')
def display_console():
    print("1) About Me")
    print("2) My Goals")
    print("3) Fun Fact")
    print("4) Exit")

while True:
    display_console()
    choice = input("Pick an option: ")

    if choice == "1":
        about_me = input("About Me: ")
    elif choice == "2":
        my_goals = input("My Goals: ")
    elif choice == "3":
        fun_fact = input("Fun fact about me: ")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please pick a valid number.")