import sys

def create_or_analyse():

    print("Do you want to create a random dataset or analyse an existing one?")
    print("type the number '1' to Create")
    print("type the number '2' to Analyse")

    n = 0 

    while n < 3:
        choice = input("Enter your choice: ")
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            n += 1
            print(f"Invalid choice. Please try again. Remaining attempts: {3-n}")
            
    print("Invalid choice. Exiting program.")
    sys.exit(1)
        