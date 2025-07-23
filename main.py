from utils.analysis.analysis import analysis
from utils.graph_choice.graph_choice import graph_choice
from utils.data_selection.data_selection import data_selection
from utils.regression_and_outliers.regression_and_outliers import regression_and_outliers
from utils.plot.plot import plot

def main():
    #readcsv file and create a dataframe
    df = analysis()

    #select type of graph
    plotinput = graph_choice()

    #ask for collumn indexes
    col1, col2 = data_selection(df, plotinput)

    #check if the user wants to remove alpha outliers and calculate regression line if applicable
    subset_df, slope, intercept = regression_and_outliers(df, col1, col2)

    #plot the data
    plot(subset_df, col1, col2, plotinput, slope, intercept)


if __name__ == "__main__":
    main()  
