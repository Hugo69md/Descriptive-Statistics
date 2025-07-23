import pandas as pd

def dfmodif(df):
   
    # Remove rows with NaN values
    df = df[df['Customer_Age'] == 40]
    #df = df[df['Month'] == 'May']
    df = df[df['Customer_Gender'] == 'M']
    df['Profit_Revenue_Product'] = df['Profit'] * df['Revenue']

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)
    
    return df