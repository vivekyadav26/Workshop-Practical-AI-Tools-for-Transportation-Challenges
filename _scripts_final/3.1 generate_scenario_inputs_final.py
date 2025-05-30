# Generate Future Scenario Inputs
import pandas as pd

def build_future_scenario(base_file):
    df = pd.read_csv(base_file)
    # Suggest a 2050 scenario with 1.25x population and 1.15x employment
    df['population_2050'] = df['population'] * 1.25
    df['employment_2050'] = df['employment'] * 1.15
    return df

df = build_future_scenario("data/zonal_data.csv")
print("Future Scenario Data (2050):")
print(df[['taz', 'population_2050', 'employment_2050']].round(1))