import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

def D_box(df, col1, col2, fig, ax, graph_dir, timestamp):
    #give path to correct directory
    sub_dir = os.path.join(graph_dir, "box")
    df = df.sort_values(by=col1)
    sns.boxplot(x=col1, y=col2, data=df, hue=col1, palette="viridis")
    ax.set_title(f"Box plot of {col1}")
    ax.set_ylabel(col1)
    ax.tick_params(axis='x', rotation=90)
    filename = os.path.join(sub_dir, f'boxplot_{timestamp}.png')
    fig.savefig(filename)
    print(f"The plot has been saved as {filename}. Thank you for using the program !.")