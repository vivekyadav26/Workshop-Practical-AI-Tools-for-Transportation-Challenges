import pandas as pd

# read project evaluation results
df = pd.read_csv("data/project_eval_results.csv")

# Group by scenario and compute summary stats
summary = df.groupby("scenario").agg({
    "avg_travel_time_to_jobs": "mean",
    "co2_emissions_kg": "sum",
    "accessibility_index": "mean"
}).reset_index()

print(summary)
