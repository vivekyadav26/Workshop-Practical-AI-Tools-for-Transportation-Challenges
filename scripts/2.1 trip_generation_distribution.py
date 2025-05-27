import pandas as pd
import numpy as np


# Create a simple trip generation model using 'zonal_data_clean.csv/zonal_data.csv'
# production = Population X 0.6 (trip rates per person)
# attractions = Employment X 0.3 + Land Use Attractions X 0.7

def generate_trips(df):
    pass

# Create a simple trip distribution model 
# Create a gravity model 
# Generate distance using Github copilot
# Friction factors is 1/ distance ^2
# Normalize the rows to match total productions
# output is a trip matrix

def distribute_trips(df):
    pass



df = pd.read_csv("data/zonal_data.csv")
df = generate_trips(df)
od_matrix = distribute_trips(df)

print("Trip Production + Attraction Data:")
print(df[["zone_id", "productions", "attractions"]])

print("\nEstimated OD Matrix:")
print(od_matrix.round(1))
