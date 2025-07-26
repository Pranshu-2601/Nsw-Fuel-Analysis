import pandas as pd
from .utils import log

def merge_geo(df_fuel, df_postcodes):
    df_postcodes['place_name'] = df_postcodes['place_name'].str.upper()

    df4 = df_fuel.merge(
        df_postcodes,
        left_on=['Postcode', 'Suburb'],
        right_on=['postcode', 'place_name'],
        how='left'
    )

    null_fields = df4[['latitude', 'longitude']].isna().any(axis=1)

    if null_fields.any():
        df3_sorted = df_postcodes.sort_values('place_name', ascending=True)
        df3_postcode_match = df3_sorted.drop_duplicates(subset=['postcode'], keep='first')
        df4_new = df4.loc[null_fields, ['Postcode']].merge(
            df3_postcode_match[['postcode', 'latitude', 'longitude']],
            left_on='Postcode',
            right_on='postcode',
            how='left'
        )
        df4.loc[null_fields, ['latitude', 'longitude']] = df4_new[['latitude', 'longitude']].values

    drop_cols = ['postcode', 'place_name', 'state_name', 'state_code']
    df4.drop(columns=drop_cols, errors='ignore', inplace=True)
    df4.to_csv('df4.csv', index=False)

    log("MERGE GEO", output_df=df4, other=df4.shape)
    return df4
