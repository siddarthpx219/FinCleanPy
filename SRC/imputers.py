from sklearn.impute import KNNImputer
import pandas as pd
import xgboost as xgb

def smart_impute(df, method="knn"):
    if method == "knn":
        imputer = KNNImputer()
        df[:] = imputer.fit_transform(df)
    elif method == "xgboost":
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                train = df[df[col].notnull()]
                test = df[df[col].isnull()]
                model = xgb.XGBRegressor()
                model.fit(train.drop(columns=[col]), train[col])
                df.loc[df[col].isnull(), col] = model.predict(test.drop(columns=[col]))
    return df