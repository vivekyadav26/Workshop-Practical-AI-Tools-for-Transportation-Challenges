# Calculate Average Trip Length from OD Matrix
import pandas as pd

def avg_trip_length(od_file):
    df = pd.read_csv(od_file)
    # OD file has origin, destination, distance_mi, trips
    # Copilot can help compute weighted average distance
    return (df['distance_mi'] * df['trips']).sum() / df['trips'].sum()

df = pd.read_csv("data/od_trips_with_distance.csv")
avg_length = avg_trip_length("data/od_trips_with_distance.csv")
print(f"Average Trip Length: {avg_length:.2f} miles")