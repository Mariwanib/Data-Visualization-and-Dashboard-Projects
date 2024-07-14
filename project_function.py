import pandas as pd

def data_trans(df, date_col, col1_obj, col2_obj):

    # Exceptions on dataframe type, column names and column input type.
    if not isinstance(df, pd.DataFrame):
        raise Exception('Incorrect DataFrame type')
    if not isinstance(date_col, str) and not isinstance(col1_obj, str) and not isinstance(col2_obj, str):
        raise Exception('The column name needs to input as string')
    column_names = df.columns
    if date_col not in column_names and col1_obj not in column_name and col2_obj not in column_name:
        raise Exception('The colum is not in the dataframe')
    
    
    # This converts date to pandas datetime and removes $ sign and comma in total gross and inflation adjusted gross.
    disney_trans = df.assign(release_date = pd.to_datetime(df[date_col]),
                             total_gross = df[col1_obj].str.replace('[$,]','',regex = True),
                             inflation_adjusted_gross = df[col2_obj].str.replace('[$,]','',regex=True))

    # Convert total_gross and inflation_adjusted_gross to int type.
    disney_trans['total_gross'] = disney_trans['total_gross'].astype('int')
    disney_trans['inflation_adjusted_gross'] = disney_trans['inflation_adjusted_gross'].astype('int')
    
    return disney_trans



