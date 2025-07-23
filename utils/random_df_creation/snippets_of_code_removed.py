#choose whether to plot the data or not

"""
print("Would you like to plot the data?")
print("type the number '1' for Yes")
print("type the number '2' for No")

n = 0 

while n < 3:
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            break
        elif choice == "2":
            print("thank you for using the program ! Exiting program.")
            sys.exit(1)
        else:
            raise ValueError
    except ValueError: 
        n += 1
        print(f"Invalid choice. Please try again. Remaining attempts: {3-n}")
    """