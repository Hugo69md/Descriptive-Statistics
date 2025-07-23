import pandas as pd
import numpy as np
import sys
from utils.random_df_creation.createarray import arraycreation


def create_random_df():

    #user select size of dataset
    print("You chose to Create a random dataset, please enter the number of rows and columns (in this order) you would like to create.")

    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))  
            break
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    print(f"the dataset will have {rows} rows and {columns} columns.")


    #user select datatype float or int
    print("which type of data would you like to create? 'True' for reel numbers or 'False' for integers.")

    while True:
        try:
            datatype = (input("True of False: ").capitalize())
            if datatype == "True":
                datatype = True
                break
            elif datatype == "False":
                datatype = False
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter True or False.")


    #user select range of values
    print("Please enter the range of values you would like to create in the dataset.")

    while True:
        try:
            min = int(input("Enter the minimum value of the range of the created dataset (must be an integer): "))
            max = int(input("Enter the maximum value of the range of the created dataset (must be an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter integers.")

    #readjusting range in case of floats due to the generation protocol
    #testmax = max - 1
    #if datatype == True and not testmax == min :
       # max -= 1
    #print(max)
    #create the array
    finalarray = arraycreation(datatype, rows, columns, min, max)

    #create the dataframe 
    df = pd.DataFrame(finalarray, columns=[f"Column_{i}" for i in range(columns)])

    #save the dataframe to a csv file
    filename = 'dataframe.csv'
    df.to_csv(filename, index=False, mode='w')
    return True