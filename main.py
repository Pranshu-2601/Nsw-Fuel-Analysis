from fuel_analysis.ingestion import load_fuel_data, clean_fuel_data, load_postcodes
from fuel_analysis.merge_geo import merge_geo
from fuel_analysis.aggregation import aggregate_fuel_prices, add_price_change_average, add_price_change_previous
from fuel_analysis.visualization import visualize_station_types, visualize_regions

if __name__ == "__main__":
    df1 = load_fuel_data("data/fuel.csv")
    df2 = clean_fuel_data(df1)
    df3 = load_postcodes("data/postcodes.json")
    df4 = merge_geo(df2, df3)
    df5 = aggregate_fuel_prices(df4)
    df6 = add_price_change_average(df4, df5)
    df7 = add_price_change_previous(df6)
    ans8 = visualize_station_types(df7)
    ans9 = visualize_regions(df7)
    print(ans8)
    print(ans9)
