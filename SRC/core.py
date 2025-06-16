import pandas as pd

def profile_data(df):
    profile = {
        'missing': df.isnull().sum(),
        'types': df.dtypes,
        'summary': df.describe(include='all')
    }
    return profile