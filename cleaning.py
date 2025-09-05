#remove rows where store was closed
def remove_closed_stores(df):
    return df[df['Open'] == 1]

def fix_holidays_column(df):
    df['State_holiday'] = df['State_holiday'].replace({'a': 1, 'b': 1, 'c': 1, '0': 0})
    df['State_holiday'] = df['State_holiday'].astype(int)
    return df