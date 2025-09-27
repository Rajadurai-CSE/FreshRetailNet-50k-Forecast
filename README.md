🛒 FreshRetailNet Sales Forecast
📌 Problem Statement

This project aims to forecast product-level demand while accounting for sales lost during stockouts through latent demand recovery. It leverages real-world features such as temperature, humidity, precipitation, and wind level that affect consumer demand.

The project uses FreshRetailNet-50K, a large-scale, real-world perishable goods sales dataset from 898 stores across 18 cities.

🎯 Objectives

Apply different methods to recover latent demand during stockout hours.

Use the modified dataset to train machine learning models.

Forecast demand at a store–product level.

📊 Dataset Summary

Source: FreshRetailNet-50K

Stores: 898

Time Window: 90 days

🔑 Key Columns

hours_sale → Units sold per hour

hours_stock_status → 1 = stockout, 0 = in-stock

discount, activity_flag → Promotion metadata

holiday_flag, precpt, avg_temperature → Contextual features

🔍 Exploratory Data Analysis (EDA)

Holiday positively impacts sales.

Temperature: Sales drop on colder days (10–15°C) compared to warmer days (20–30°C).

Humidity: Low humidity correlates with lower sales.

Activity Flag: Promotions significantly increase sales.

Precipitation: Minimal impact on sales.

Time of Day: Higher sales in morning and afternoon.

Day of Week: Weekends see more sales than weekdays.

📈 Sample Visualizations
<img width="737" height="540" alt="image" src="https://github.com/user-attachments/assets/9dd69f33-9a2d-4fa0-b421-425e2b90037b" /> <img width="774" height="537" alt="image" src="https://github.com/user-attachments/assets/e09b730a-7609-4b78-bebf-4300ca1fe1d7" /> <img width="725" height="562" alt="image" src="https://github.com/user-attachments/assets/51606dc5-209a-4a8a-98aa-dc7ab930ce49" /> <img width="737" height="549" alt="image" src="https://github.com/user-attachments/assets/b5503ed5-918c-4fbc-95cc-73a972ca8f85" />
✅ Results
<img width="1919" height="900" alt="FreshRet-1" src="https://github.com/user-attachments/assets/e0f2c4ef-4a34-446c-b44d-f7b0643232f5" />

🚀 How to Use

Clone the Repository

git clone https://github.com/Rajadurai-CSE/FreshRetailNet-50k-Forecast.git
cd FreshRetailNet-EndtoEnd


Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Launch the Streamlit App

cd streamlit-app
streamlit run app.py

🔮 Future Enhancements

Experiment with advanced strategies for latent demand recovery.

Forecast at the category level instead of only SKU level.

Incorporate deep learning models (e.g., LSTMs, Transformers).

Enhance app with interactive model comparison and dashboards.

🙌 Acknowledgements

Dataset: FreshRetailNet-50K

Libraries: Pandas, Scikit-learn, XGBoost, LightGBM, Streamlit

✨ Thank you for exploring this project!
