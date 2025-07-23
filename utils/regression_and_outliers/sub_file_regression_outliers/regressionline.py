import pandas as pd
from sklearn.linear_model import LinearRegression #type: ignore[import]
import numpy as np

def regressionline(subset_df, col1, col2):
    # Get the data as 1D arrays first
    X_raw = subset_df[col1].values
    y_raw = subset_df[col2].values
    
    # Convert to numeric
    X_raw = pd.to_numeric(X_raw, errors='coerce')
    y_raw = pd.to_numeric(y_raw, errors='coerce')
    
    #Find valid indices (both X and y are not NaN)
    valid_indices = ~np.isnan(X_raw) & ~np.isnan(y_raw)
    
    # Filter the data
    X_filtered = X_raw[valid_indices]
    y_filtered = y_raw[valid_indices]
    
    #Check if we have valid data
    if len(X_filtered) == 0:
        raise ValueError("No valid data available for regression.")
    
    # Reshape X for sklearn (needs to be 2D)
    X_reshaped = X_filtered.reshape(-1, 1)
    
    # Create the model
    model = LinearRegression()
    model.fit(X_reshaped, y_filtered)
    
    return model.coef_, model.intercept_