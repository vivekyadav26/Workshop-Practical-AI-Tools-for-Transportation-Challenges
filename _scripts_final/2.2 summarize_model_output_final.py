# Summarize Model Outputs
import pandas as pd

def summarize_model_data(file_path):
    df = pd.read_csv(file_path)
    # Let Copilot suggest summaries by TAZ or corridor: total VMT, delay, etc.
    summary = df.groupby('corridor')[['vmt','delay_min']].sum().reset_index()
    return summary

summary = summarize_model_data("data/model_output.csv")
print("Model Output Summary by Corridor:")
print(summary.round(1))