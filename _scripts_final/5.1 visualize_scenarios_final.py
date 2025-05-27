import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the evaluation summary data from CSV
df = pd.read_csv("data/project_eval_results.csv")

# Group the data by scenario and calculate average metrics
summary = df.groupby("scenario").mean(numeric_only=True).reset_index()

# Set a clean seaborn style for the plots
sns.set(style="whitegrid")

# Create a row of 3 subplots for CO2, travel time, and accessibility
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Bar chart of average CO2 emissions by scenario
sns.barplot(data=summary, x="scenario", y="co2_emissions_kg", ax=axes[0], palette="Reds")
axes[0].set_title("Average CO2 Emissions by Scenario")
axes[0].set_ylabel("kg")

# Bar chart of average travel time by scenario
sns.barplot(data=summary, x="scenario", y="avg_travel_time_to_jobs", ax=axes[1], palette="Blues")
axes[1].set_title("Avg Travel Time to Jobs")
axes[1].set_ylabel("Minutes")

# Bar chart of accessibility index by scenario
sns.barplot(data=summary, x="scenario", y="accessibility_index", ax=axes[2], palette="Greens")
axes[2].set_title("Accessibility Index")
axes[2].set_ylabel("Index")

# Adjust layout for better spacing
plt.tight_layout()

plt.show()