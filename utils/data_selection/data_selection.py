import pandas as pd
from utils.data_selection.one_column_case.one_column_selection import one_column_selection
from utils.data_selection.two_columns_case.two_columns_selection import two_columns_selection

def data_selection(df, plotinput):
    while True:
        if plotinput == 5 :
            try: 
                huechhoice = input("Do you want to apply a hue to the distribution plot ? (yes/no): ").strip().lower()
                if huechhoice == 'no':
                    col1, col2 = one_column_selection(df)
                elif huechhoice == 'yes':
                    print("You chose to apply a hue to the distribution plot, the First column will be used as the data and the second as hue.")
                    col1, col2 = two_columns_selection(df)
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue          
        else:
            col1, col2 = two_columns_selection(df)

        return col1, col2