import pandas as pd
import numpy as np
from .utils import log

def aggregate_fuel_prices(df4):
    df4['PriceUpdatedDate'] = df4['PriceUpdatedDate'].astype('datetime64[ns]')
    daily_avg_station = df4.groupby(['Postcode','FuelCode','PriceUpdatedDate','Name']).agg({'Price':'mean'})
    daily_avg_postcode = daily_avg_station.groupby(['Postcode','FuelCode','PriceUpdatedDate']).agg({'Price':'mean'})
    final_avg = daily_avg_postcode.groupby(['Postcode','FuelCode']).agg({'Price':'mean'}).reset_index()
    final_avg = final_avg.rename(columns={'FuelCode':'FuelType','Price':'AveragePrice'})
    final_avg['AveragePrice'] = np.round(final_avg['AveragePrice'],2)
    multi_index = pd.MultiIndex.from_product(
        [df4['Postcode'].unique(), df4['FuelCode'].unique()],
        names=['Postcode','FuelType']
    )
    df5 = final_avg.set_index(['Postcode','FuelType']).reindex(multi_index, fill_value=0.00)
    df5.sort_index(level=['Postcode','FuelType'], inplace=True)
    df5.to_csv('df5.csv')
    log("AGGREGATE FUEL PRICES", output_df=df5, other=df5.shape)
    return df5

def add_price_change_average(df4, df5):
    df6 = df4.merge(df5, left_on=["Postcode","FuelCode"], right_index=True, how="left")
    df6["PriceChangeAverage"] = ((df6["Price"] - df6["AveragePrice"]) / df6["AveragePrice"]) * 100
    df6["PriceChangeAverage"] = np.round(df6["PriceChangeAverage"], 2)
    df6.drop(columns=['AveragePrice'], inplace=True)
    df6.to_csv('df6.csv', index=False)
    log("ADD PRICE CHANGE AVG", output_df=df6, other=df6.shape)
    return df6

def add_price_change_previous(df6):
    df7 = df6.sort_values(by=["Address","FuelCode","PriceUpdatedDate"])
    df7["PriceChangePrevious"] = df7.groupby(["Address","FuelCode"])['Price'].diff().fillna(0)
    df7["PriceChangePrevious"] = np.round(df7["PriceChangePrevious"], 2)
    log("ADD PRICE CHANGE PREV", output_df=df7, other=df7.shape)
    return df7
