# Autogenerate Markdown Summary
import pandas as pd

# write summary function to show the total vmt, delay_min, average trip length , volume 

def write_summary(stats_dict):
    summary = f"""
    ## LRTP Summary
    - Total Vehicle Miles Traveled: {stats_dict['vmt']:,}
    - Total Delay (minutes): {stats_dict['delay_min']:,}
    - Average Trip Length: {stats_dict['distance']:.2f} mi
    - Average Daily Volume: {stats_dict['volume']:,}
    """
    with open("summary.md", "w") as f:
        f.write(summary)

# Load the evaluation results data from CSV
df = pd.read_csv("data/model_output.csv")

# calculate total vmt and average delay_min, distance, volume
summary = df[[ 'delay_min', 'distance', 'volume']].mean(numeric_only=True)
summary['vmt'] = df['vmt'].sum()  # Total VMT

print(summary)
write_summary(summary)