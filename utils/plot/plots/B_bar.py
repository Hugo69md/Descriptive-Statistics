import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

def B_bar(df, col1, col2, fig, ax, graph_dir, timestamp):
    #give path to correct directory
    sub_dir = os.path.join(graph_dir, "bar")
    sum_df = df.groupby(col1)[col2].sum().reset_index()                                                                 #sum the value of col2 for each unique value of col1
    sum_df = sum_df.sort_values(by=col1)                                                                                #sort the dataframe by col1 names
    ax = sns.barplot(x=col1, y=col2, data=sum_df, hue=col1, palette="viridis")                                          #create a bar plot,
    for label in ax.containers:                                                                                         #add values to the bars
        ax.bar_label(label, fontsize=10, labels=[f'{v}' for v in label.datavalues], padding=3, rotation=60)             #rotate the labels for better readability 
    ax.set_title(f"Bar plot of {col1} and {col2}")                                                                      #set the title of the plot and x and y labels                    
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.tick_params(axis='x', rotation=90)                                                                               #rotate the x labels for better readability                  
    filename = os.path.join(sub_dir, f'barplot_{timestamp}.png')                                                      #save the plot in the graphs directory with a timestamp                     
    fig.savefig(filename)
    print(f"The plot has been saved as {filename}. Thank you for using the program !.")