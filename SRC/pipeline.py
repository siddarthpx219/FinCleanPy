from .core import profile_data
from .imputers import smart_impute
from .anomaly import remove_outliers

class CleanPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, name, **kwargs):
        self.steps.append((name, kwargs))

    def run(self, df):
        for name, kwargs in self.steps:
            if name == "profile":
                profile_data(df)
            elif name == "smart_impute":
                df = smart_impute(df, **kwargs)
            elif name == "remove_outliers":
                df = remove_outliers(df, **kwargs)
            elif name == "normalize":
                df = (df - df.mean()) / df.std()
        return df
