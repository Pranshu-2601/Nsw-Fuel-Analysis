import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .utils import log, studentid

def visualize_station_types(df7):
    df7["Price"] = df7["Price"].astype(float)
    df7["PriceChangeAverage"] = df7["PriceChangeAverage"].astype(float)
    df7["PriceChangePrevious"] = df7["PriceChangePrevious"].astype(float)
    df7["s_type"] = df7["Brand"].apply(lambda x: "Independent" if x.lower() == "independent" else "Franchised")

    df8 = df7.groupby("s_type").agg(AvgPrice=("Price","mean"), MaxPrice=("Price","max"), Count=("s_type","size")).reset_index()
    df8 = df8.iloc[::-1].reset_index(drop=True)

    fig, ax = plt.subplots(1, 3, figsize=(20,7))
    bar_width = 0.3
    x = range(len(df8["s_type"]))
    b1 = ax[0].bar(x, df8["AvgPrice"], width=bar_width, color='teal', label="Avg Price")
    b2 = ax[0].bar([p + bar_width for p in x], df8["MaxPrice"], width=bar_width, color='coral', label="Max Price")
    for bars in [b1,b2]:
        for j in bars:
            ax[0].text(j.get_x()+j.get_width()/2, j.get_height()+0.02, f"{j.get_height():.2f}", ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax[0].set_title("Avg & Max Fuel Price: Independent vs Franchised", fontsize=15, fontweight='bold')
    ax[0].set_ylabel("Price (¢)", fontsize=14)
    ax[0].set_xlabel("Station Type", fontsize=14)
    ax[0].set_xticks([p + bar_width/2 for p in x])
    ax[0].set_xticklabels(df8["s_type"], fontsize=14, fontweight='bold')
    ax[0].legend()

    threshold = df7["Price"].median()
    df7["price_category"] = df7["Price"].apply(lambda x: "High" if x > threshold else "Low")
    df_counts = df7.groupby(["s_type","price_category"]).size().unstack(fill_value=0)
    colors = {"High":"coral","Low":"teal"}
    for i, station_type in enumerate(df_counts.index):
        wedges, texts, autotexts = ax[i+1].pie(
            df_counts.loc[station_type],
            labels=[f"{lbl} Price" for lbl in df_counts.columns],
            autopct='%1.1f%%',
            colors=[colors[lbl] for lbl in df_counts.columns],
            startangle=90,
            radius=0.85,
            textprops={'fontsize':14},
            wedgeprops={'edgecolor':'black'}
        )
        for autotext in autotexts: autotext.set_fontsize(14)
        ax[i+1].text(0, -1.2, f"{station_type} Stations", ha='center', fontsize=14, fontweight='bold')

    plt.subplots_adjust(wspace=0.5)
    plt.tight_layout()
    plt.savefig(f"Station Type Visulization.png")

    answer8 = "Independent stations generally have cheaper prices..."
    log("VISUALIZE STATION TYPES", other=answer8)
    return answer8

def visualize_regions(df7):
    df7['Price'] = df7['Price'].astype(float)
    df7['Postcode'] = df7['Postcode'].astype(int)
    df7['PriceUpdatedDate'] = df7['PriceUpdatedDate'].astype('datetime64[ns]')
    df7['Region'] = pd.cut(df7['Postcode'],
                           bins=[-float('inf'),2199,2499,float('inf')],
                           labels=["Metro Area Sydney","Inner Regional","Outer Regional"])
    avg_prices = df7.groupby('Region', observed=False)['Price'].mean()
    region_counts = df7['Region'].value_counts()
    order = ["Metro Area Sydney","Inner Regional","Outer Regional"]
    avg_prices = avg_prices.reindex(order)
    region_counts = region_counts.reindex(order, fill_value=0)

    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    bars = ax[0].bar(avg_prices.index, avg_prices, color=['blue','gray','orange'])
    ax[0].set_title('Average Fuel Price by Region', fontsize=15, fontweight='bold')
    ax[0].set_ylabel('Average Price (¢)', fontsize=15)
    ax[0].set_xlabel('Region', fontsize=15)
    ax[0].set_xticks(range(len(avg_prices.index)))
    ax[0].set_xticklabels(avg_prices.index, fontweight='bold')
    for b in bars:
        ax[0].text(b.get_x()+b.get_width()/2, b.get_height(), f'{b.get_height():.2f}', ha='center', va='bottom', fontsize=15, fontweight='bold')
    ax[1].pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140, colors=['blue','gray','orange'], wedgeprops={'edgecolor':'black'})
    ax[1].set_title('Proportion of Records by Region', fontsize=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"Region Visualization.png")

    answer9 = "Outer Regional areas have highest prices despite fewer records..."
    log("VISUALIZE REGIONS", other=answer9)
    return answer9
