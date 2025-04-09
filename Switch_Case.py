from datetime import datetime

def say_hello():
    print("👋 Hello there!")

def show_time():
    print("⏰ Current time:", datetime.now().strftime("%H:%M:%S"))

def exit_program():
    print("👋 Goodbye! See you again.")

def default_case():
    print("❌ Invalid choice. Please try again.")

def menu():
    print("\n📋 Menu:")
    print("1. Say Hello")
    print("2. Show Time")
    print("3. Exit")

# Dictionary simulating switch-case
switch_dict = {
    "1": say_hello,
    "2": show_time,
    "3": exit_program
}

# Main loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "3":
        switch_dict[choice]()
        break  # Exit the loop

    # Call the corresponding function
    switch_dict.get(choice, default_case)()
