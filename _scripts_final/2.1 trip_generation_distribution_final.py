import pandas as pd
import numpy as np


# Create a simple trip generation model using 'zonal_data_clean.csv/zonal_data.csv'
# production = Population X 0.6 (trip rates per person)
# attractions = Employment X 0.3 + Land Use Attractions X 0.7

def generate_trips(df):
    # Trip productions are proportional to population
    df["productions"] = df["population"] * 0.6  # 0.6 trips per person
    # Trip attractions based on employment and land use attractiveness
    df["attractions"] = df["employment"] * 0.3 + df["attractions"] * 0.7
    return df

# Create a simple trip distribution model
# Create a gravity model
# Generate synthetic impedance (squared distance matrix)
# Friction factors is 1/ distance ^2
# Normalize the rows to match total productions
# output is a trip matrix

def distribute_trips(df):
    zones = df["taz"].values        
    prod = df["productions"].values
    attr = df["attractions"].values
    # Gravity model using synthetic impedance (squared distance matrix) based on length of zones
    # create 10 x 10 distance matrix with random values
    dist_matrix = np.array([
        [1, 2, 4, 3, 1, 2, 3, 4, 5, 1],
        [2, 1, 3, 2, 4, 5, 1, 2, 3, 4],
        [4, 3, 1, 5, 2, 1, 2, 3, 4, 5],
        [3, 2, 5, 1, 3, 4, 5, 1, 2, 3],
        [1, 4, 2, 3, 5, 1, 2, 4, 3, 5],
        [2, 3, 4, 5, 1, 2, 3, 4, 5, 1],
        [1, 2, 3, 4, 2, 3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
        [3, 1, 2, 4, 5, 1, 2, 3, 4, 5],
        [2, 4, 5, 3, 1, 2, 3, 4, 5, 1]
    ])
    friction = 1 / (dist_matrix ** 2)
    # Compute raw trip matrix
    trip_matrix = np.outer(prod, attr) * friction
    # Normalize rows to match total productions
    row_sums = trip_matrix.sum(axis=1, keepdims=True)   
    trip_matrix = np.divide(trip_matrix, row_sums, where=row_sums != 0) * prod[:, np.newaxis]

    return pd.DataFrame(trip_matrix, index=zones, columns=zones)


df = pd.read_csv("data/zonal_data.csv")
df = generate_trips(df)
od_matrix = distribute_trips(df)

print("Trip Production + Attraction Data:")
print(df[["taz", "productions", "attractions"]])

print("\nEstimated OD Matrix:")
print(od_matrix.round(1))
