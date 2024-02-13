import pandas as pd

# Function for replaceing all empty with na
def replace_empty(df):
    col = df.columns
    for i in range(len(col)):
        name = col[i]
        df[name] = df[name].replace('', pd.NA)

# Function that count all nah/na values
def get_na_count(df):
    col = df.columns
    counts = {}
    for i in range(len(col)):
        name = col[i]
        counts[name] = df[name].isna().sum()
    return counts 
