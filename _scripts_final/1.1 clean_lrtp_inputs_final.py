# Clean LRTP Inputs
import pandas as pd


# some clean up suggestions
def clean_lrtp_inputs(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # 1. Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 2. Drop rows missing critical fields
    df = df.dropna(subset=["taz", "population", "employment"])

    # 3. Convert data types
    df["taz"] = df["taz"].astype(int)
    df["population"] = df["population"].astype(int)
    df["employment"] = df["employment"].astype(int)

    # 4. Filter out unrealistic values
    df = df[df["population"] < 100000]  # outlier removal

    # 5. Create useful new variable
    df["pop_emp_ratio"] = df["population"] / df["employment"].replace(0, pd.NA)

    return df


input_file = r"data/scenario_inputs_raw.csv"
# Call the function and save the cleaned data
cleaned_data = clean_lrtp_inputs(input_file)
# Save the cleaned data to a new CSV file
cleaned_data.to_csv("data/outputs/scenario_inputs_clean.csv", index=False)
# Display the first few rows of the cleaned data
print(cleaned_data.head())