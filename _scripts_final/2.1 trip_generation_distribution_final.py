import pandas as pd
import numpy as np

def generate_trips(df):
    # Trip productions are proportional to population
    df["productions"] = df["population"] * 0.6  # 0.6 trips per person
    
    # Trip attractions based on employment and land use attractiveness
    df["attractions"] = df["employment"] * 0.3 + df["attractions"] * 0.7
    return df

def distribute_trips(df):
    zones = df["zone_id"].values
    prod = df["productions"].values
    attr = df["attractions"].values
    
    # Gravity model using synthetic impedance (squared distance matrix)
    dist_matrix = np.array([
        [1, 2, 4, 3],
        [2, 1, 3, 2],
        [4, 3, 1, 5],
        [3, 2, 5, 1]
    ])
    friction = 1 / (dist_matrix ** 2)

    # Compute raw trip matrix
    trip_matrix = np.outer(prod, attr) * friction

    # Normalize rows to match total productions
    row_sums = trip_matrix.sum(axis=1, keepdims=True)
    trip_matrix = np.divide(trip_matrix, row_sums, where=row_sums != 0) * prod[:, np.newaxis]
    
    return pd.DataFrame(trip_matrix, index=zones, columns=zones)

if __name__ == "__main__":
    df = pd.read_csv("data/zonal_data.csv")
    df = generate_trips(df)
    od_matrix = distribute_trips(df)
    
    print("Trip Production + Attraction Data:")
    print(df[["zone_id", "productions", "attractions"]])
    
    print("\nEstimated OD Matrix:")
    print(od_matrix.round(1))
