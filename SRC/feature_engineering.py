def add_rolling_features(df, col, window=5):
    df[f"{col}_rolling_mean"] = df[col].rolling(window).mean()
    return df