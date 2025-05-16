# Calculate Average Trip Length from OD Matrix
import pandas as pd

def avg_trip_length(od_file):
    df = pd.read_csv(od_file)
    # OD file has origin, destination, distance_km, trips
    # Copilot can help compute weighted average distance
    return (df['distance_km'] * df['trips']).sum() / df['trips'].sum()