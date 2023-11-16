
def check_data():
    try:
        name = input("Enter your name: ")
        if name.isalpha():
            print("You have a valid name.")
        else:
            print("Invalid data")
    except KeyboardInterrupt:
        print("\nProcess Interrupted")

check_data()