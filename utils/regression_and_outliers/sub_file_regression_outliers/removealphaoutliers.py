import pandas as pd

"""
Remove outliers from the specified columns of a DataFrame based on an alpha value.
Parameters:
col1 (str): The name of the first column to check for outliers.
col2 (str): The name of the second column to check for outliers (optional).
df (pd.DataFrame): The DataFrame from which to remove outliers.
Returns:
pd.DataFrame: A DataFrame with outliers removed based on the specified alpha value.
"""

def removealphaoutliers(col1, col2, df):
    dfoutliers = df.copy()
    if col2 is not None:
        for col in [col1, col2]:
            if pd.api.types.is_numeric_dtype(dfoutliers[col]):
                alpha = int(input("what is the alpha value for outlier detection?, input a number between 0 and 100: "))
                if not (0 <= alpha <= 100):
                    print("Invalid alpha value. Please enter a number between 0 and 100.")
                    continue
                else:
                    alphadiv2 = alpha / 200
                dfoutliers = dfoutliers[(dfoutliers[col] >= dfoutliers[col].quantile(alphadiv2)) & (dfoutliers[col] <= dfoutliers[col].quantile(1-alphadiv2))]
                print(f"Outliers in column '{col}' have been removed using alpha value {alpha}.")
            else:
                print(f"Column '{col}' is not numeric, skipping outlier removal.")
    else:
        if pd.api.types.is_numeric_dtype(dfoutliers[col1]):
            alpha = int(input("what is the alpha value for outlier detection?, input a number between 0 and 100: "))
            if not (0 <= alpha <= 100):
                print("Invalid alpha value. Please enter a number between 0 and 100.")
            else:
                alphadiv2 = alpha / 200
                dfoutliers = dfoutliers[(dfoutliers[col1] >= dfoutliers[col1].quantile(alphadiv2)) & (dfoutliers[col1] <= dfoutliers[col1].quantile(1-alphadiv2))]
                print(f"Outliers in column '{col1}' have been removed using alpha value {alpha}.")
        else:
            print(f"Column '{col1}' is not numeric, skipping outlier removal.")

    return dfoutliers

   