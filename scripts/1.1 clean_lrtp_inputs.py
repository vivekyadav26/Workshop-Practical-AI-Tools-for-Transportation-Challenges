# Clean LRTP Inputs
import pandas as pd

# define a function to read the 'scenario_inputs_raw.csv' file. 
# the function should check for nulls, rename columns, strip text 
# and filter at zones with population greater 10,000 
# save the data as 'scenario_inputs_clean.csv'
# create a new column 'pop_emp_ratio' which is ratio of population to employments.

def clean_inputs(file_path):
    df = pd.read_csv(file_path)
    # Let Copilot suggest the rest
    # test the code
    # iterate till all errors are fixed
    return df


# call the clean_inputs function
# display results
