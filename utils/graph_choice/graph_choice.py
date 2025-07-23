def graph_choice():
    print("What type of plot would you like to create? among Scatter (press 1), Bar plot (press 2), Line plot (press 3), boxplot (press 4) and distribution plot (press 5).")
    while True:
        try:
            plotinput = int(input("Enter your choice: "))
            if plotinput in range(1,6):
                if plotinput == 2:
                    print("You have selected a bar plot, make sure to select an Object column for the X axis")
                elif plotinput == 4:
                    print("You have selected a box plot, make sure to select an Object column for the X axis")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    return plotinput