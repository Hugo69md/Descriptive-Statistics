import pandas as pd
from utils.___dfmodification.dfmodif import dfmodif

def analysis():

    dfnew = pd.read_csv('dataframe.csv')

    #call the modification function to modify the dataframe
    df = dfmodif(dfnew)

    #displays info about df
    print(df.head())
    print("Here are some statistics about the dataset:")
    print(df.describe())
    print("Here are some infos about the dataset:")
    print(df.info())

    return df
    