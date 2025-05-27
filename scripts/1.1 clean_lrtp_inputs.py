# Clean LRTP Inputs
import pandas as pd

# define a function to read the 'scenario_inputs_raw.csv' file. 
# the function should check for nulls, drop columns if the important columns have
# Nulls, strip text from column names, convert columns to appropriate data types,
# and filter at zones with population greater 10,000 
# create a new column 'pop_emp_ratio' which is ratio of population to employments.
# save the data as 'scenario_inputs_clean.csv'


def clean_inputs(file_path):
    df = pd.read_csv(file_path)
    # Let Copilot suggest the rest
    # test the code
    # iterate till all errors are fixed

    # Check for nulls

    return df


# read the 'scenario_inputs_raw.csv' file
# call the clean_inputs function
# display results
