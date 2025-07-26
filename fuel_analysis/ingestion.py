import pandas as pd
from .utils import log

def load_fuel_data(fuel_csv):
    df = pd.read_csv(fuel_csv, on_bad_lines=lambda x: x[1:] if len(x) == 9 else x, engine='python')
    log("LOAD FUEL DATA", output_df=df, other=df.shape)
    return df

def clean_fuel_data(df):
    df2 = (
        df.rename(columns={"ServiceStationName": "Name"})
          .assign(Suburb=df['Suburb'].str.upper())
          .query("Address.str.contains(r'\\bNSW\\b', case=False, na=False) or "
                 "Address.str.contains('new south wales', case=False, na=False)", engine="python")
    )
    log("CLEAN FUEL DATA", output_df=df2, other=df2.shape)
    return df2

def load_postcodes(postcodes_json):
    df3 = pd.read_json(postcodes_json).drop(columns=["accuracy"])
    log("LOAD POSTCODES", output_df=df3, other=df3.shape)
    return df3
