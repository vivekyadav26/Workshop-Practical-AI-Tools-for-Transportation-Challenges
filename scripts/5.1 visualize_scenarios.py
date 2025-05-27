import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the evaluation results data from CSV - project_eval_results.csv
df = pd.read_csv("data/project_eval_results.csv")

# Group the data by scenario and calculate average metrics
summary = df.groupby("scenario").mean(numeric_only=True).reset_index()

# visualize the results