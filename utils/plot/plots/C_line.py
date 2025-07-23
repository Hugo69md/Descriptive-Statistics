import seaborn as sns
import matplotlib.pyplot as plt
import os

def C_line(df, col1, col2, slope, intercept, fig, ax, graph_dir, timestamp):
    #give path to correct directory
    sub_dir = os.path.join(graph_dir, "line")
    
    sns.lineplot(x=col1, y=col2, data=df)
    if slope is not None and intercept is not None:
        regression_choice = input("You chose to plot a line plot. do you want to add a regression line? (yes/no): ")

        #Ask the user if they want to add a regression line
        if regression_choice.lower() == 'yes':
               # Add the regression line to the line plot
            plt.plot(df[col1], slope[0] * df[col1] + intercept, color='red', label=f'Regression line:\nA = {slope[0]:.5f} \nB = {intercept:.5f}')
            plt.legend()
            print("Regression line has been added to the line plot.")

        else:
            print("No regression line will be added to the line plot.")

    ax.set_title(f"Line plot of {col1} and {col2}")
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    filename = os.path.join(sub_dir, f'lineplot_{timestamp}.png')
    fig.savefig(filename)
    print(f"The plot has been saved as {filename}. Thank you for using the program !.")