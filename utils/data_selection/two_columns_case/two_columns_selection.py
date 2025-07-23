import sys
import pandas as pd
from utils.data_selection.two_columns_case.indexcollumns import indexcollumns

def two_columns_selection(df):
    try: 
        collist = indexcollumns()
        col1 = df.columns[collist[0]-1]
        col2 = df.columns[collist[1]-1]
    except IndexError:
        print("Invalid input. Please enter correct column indexes.")
                
    return col1, col2