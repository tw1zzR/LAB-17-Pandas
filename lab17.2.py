import numpy as np; import pandas as pd; import json

# Reading and assign data
data = np.genfromtxt('data.txt', dtype=int)
ser = pd.Series(data.flatten())

# Find unique values
unique_values = ser.unique()

# Saving
with open('array.json', 'w') as f:
    json.dump(unique_values.tolist(), f)