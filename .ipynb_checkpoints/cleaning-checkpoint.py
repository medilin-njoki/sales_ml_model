#remove rows where store was closed
def remove_closed_stores(df):
    return df[df['Open'] == 1]

def fix_holidays_column(df):
    return df['State_holiday'].replace({'a': 1, 'b': 1, 'c': 1, '0': 0}).astype(int)

def drop_closed_rows(df, open_col="Open"):
    return df[df[open_col] != 0].copy()

def date_features(df, date_col="Date"):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day
    return df