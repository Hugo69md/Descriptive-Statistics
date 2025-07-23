import seaborn as sns
import matplotlib.pyplot as plt
import os

def E_distribution(df, col1, col2, fig, ax, graph_dir, timestamp):
    #give path to correct directory
    sub_dir = os.path.join(graph_dir, "distribution")
    if col2 is None:
        sns.displot(data=df, x=col1, kde=True,)
        plt.suptitle(f"Distribution plot of {col1}", y=1)
        fig.subplots_adjust(top=0.9)
        filename = os.path.join(sub_dir, f'distributionplot_{timestamp}.png')
        plt.savefig(filename)
        print(f"The plot has been saved as {filename}. Thank you for using the program !.")
    else:
        sns.displot(data=df, x=col1, kde=True, hue=col2) # Plot distribution with hue, it add a variable to the distribution plot
        plt.suptitle(f"Distribution plot of {col1}, using {col2} as hue", y=1)
        fig.subplots_adjust(top=0.9)
        filename = os.path.join(sub_dir, f'distributionplot_{timestamp}.png')
        plt.savefig(filename)
        print(f"The plot has been saved as {filename}. Thank you for using the program !.")