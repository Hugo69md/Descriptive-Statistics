import sys
import pandas as pd
from utils.data_selection.one_column_case.indexcollumn import indexcollumn

def one_column_selection(df):
    try: 
        collist = indexcollumn()
        col1 = df.columns[collist[0]-1]
        col2 = None  # No second column for single column selection 
    except IndexError:
        print("Invalid input. Please enter correct column indexes.")
                
    return col1, col2