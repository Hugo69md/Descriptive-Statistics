import matplotlib.pyplot as plt
import datetime
from utils.plot.plots.A_scatter import A_scatter  # Import the A_scatter function from the A_scatter module
from utils.plot.plots.B_bar import B_bar  # Import the B_bar function from the B_bar module
from utils.plot.plots.C_line import C_line  # Import the C_line function from the C_line module
from utils.plot.plots.D_box import D_box  # Import the D_box function from the D_box module
from utils.plot.plots.E_distribution import E_distribution  # Import the E_distribution function from the E_distribution module

def plot(df, col1, col2, plotinput, slope, intercept):

    fig, ax = plt.subplots(figsize=(20, 20))
    graph_dir = "graphs"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if plotinput == 1:
        A_scatter(df, col1, col2, slope, intercept, fig, ax, graph_dir, timestamp)  # Call the scatter plot function

    elif plotinput == 2:
        B_bar(df, col1, col2, fig, ax, graph_dir, timestamp)

    elif plotinput == 3:
        C_line(df, col1, col2, slope, intercept, fig, ax, graph_dir, timestamp)

    elif plotinput == 4:
        D_box(df, col1, col2, fig, ax, graph_dir, timestamp)

    elif plotinput == 5:
        E_distribution(df, col1, col2, fig, ax, graph_dir, timestamp)
