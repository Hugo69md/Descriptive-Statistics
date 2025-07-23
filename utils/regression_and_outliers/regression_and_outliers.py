from utils.regression_and_outliers.sub_file_regression_outliers.regressionline import regressionline
from utils.regression_and_outliers.sub_file_regression_outliers.removealphaoutliers import removealphaoutliers
import pandas as pd


def regression_and_outliers(df, col1, col2):
     #check if the selected columns are numeric and remove outliers if applicable,
    if col2 is not None:
        subset_df = df[[col1, col2]].copy()
        subset_df = removealphaoutliers(col1, col2, subset_df) 
        #calculate regression line if applicable
        try:
            slope, intercept = regressionline(subset_df, col1, col2)
            print(f"Regression line calculated with slope: {slope[0]}, intercept: {intercept}")
        except ValueError as e:
            slope, intercept = None, None
            
    #remove outliers if only one column is selected
    else : 
        col2 = None
        slope, intercept = None, None
        subset_df = df[[col1]].copy()
        subset_df = removealphaoutliers(col1, col2, subset_df)

    return subset_df, slope, intercept