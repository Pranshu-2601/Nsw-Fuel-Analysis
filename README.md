# ⛽ Fuel Analysis NSW

Analyze and visualize fuel pricing trends across New South Wales (NSW), Australia.  
This project combines the NSW FuelCheck dataset with postcode geolocation data to uncover insights about fuel pricing patterns.

---

## ✨ Features

✅ Load and clean fuel price data  
✅ Merge with postcode geolocation (latitude & longitude)  
✅ Calculate average fuel prices per postcode and fuel type  
✅ Compute price change percentages compared to averages and previous updates  
✅ Generate clear visualizations:
- 📉 Independent vs Franchised stations
- 🌏 Metro vs Regional NSW pricing

The project is written in **Python 3.13+** using **pandas**, **numpy**, and **matplotlib**.
---

## 📂 Project Structure

fuel-analysis/
│
├── data/ # input data files
│ ├── fuel.csv
│ └── postcodes.json
│
├── fuel_analysis/ # Python package
│ ├── ingestion.py # load and clean data
│ ├── merge_geo.py # merge geo information
│ ├── aggregation.py # calculate averages and changes
│ ├── visualization.py # create and save plots
│ ├── utils.py # shared helpers
│ └── init.py
│
├── main.py # entry point
├── requirements.txt
└── README.md

---

## 📦 Installation

1. Clone the repository:  
git clone https://github.com/<your-username>/fuel-analysis.git  
cd fuel-analysis  

2. Set up a virtual environment:  
python3 -m venv venv  
source venv/bin/activate      # On Linux/Mac  
venv\Scripts\activate         # On Windows  

3. Install dependencies:  
pip install -r requirements.txt  

---

## ▶️ Running the Analysis

1. Place the input data in the data/ folder:  
fuel.csv – NSW FuelCheck dataset  
postcodes.json – Postcodes with lat/long data  

2. Run the main script:  
python main.py  

---

## 📊 Outputs

✅ Intermediate CSVs  
df4.csv – fuel data with latitude/longitude  
df5.csv – aggregated average prices  
df6.csv – price change compared to averages  

✅ Visualizations  
Station Type Visulization.png – Independent vs Franchised station comparison  
Region Visualization.png – Metro vs Regional pricing comparison  

✅ Console summaries  
Key insights from both visualizations are printed after execution.

---

**Happy Analyzing! 🚀**
