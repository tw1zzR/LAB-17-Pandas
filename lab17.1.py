import pandas as pd

df = pd.read_csv('weight.csv')

df['LoadMass'] = df['LoadCapacity'] * df['NumFlights']

df.to_csv('auto.csv', sep='\t')

print("Results have been written to auto.csv")