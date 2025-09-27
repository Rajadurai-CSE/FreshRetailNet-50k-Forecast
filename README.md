# 🛒 FreshRetailNet Sales Forecast

## 📌 Problem Statement

This project aims to **forecast product-level demand** while accounting for sales lost during stockouts through **latent demand recovery**. It leverages real-world features such as temperature, humidity, precipitation, and wind level that affect consumer demand.

The project uses **FreshRetailNet-50K**, a large-scale, real-world perishable goods sales dataset from **898 stores across 18 cities**.

## 🎯 Objectives

1. Apply different methods to **recover latent demand** during stockout hours
2. Use the modified dataset to train **machine learning models**
3. Forecast demand at a **store–product level**

## 📊 Dataset Summary

- **Source**: FreshRetailNet-50K
- **Stores**: 898
- **Time Window**: 90 days

### 🔑 Key Columns

- `hours_sale` → Units sold per hour
- `hours_stock_status` → 1 = stockout, 0 = in-stock
- `discount`, `activity_flag` → Promotion metadata
- `holiday_flag`, `precpt`, `avg_temperature` → Contextual features

## 🔍 Exploratory Data Analysis (EDA)

1. **Holiday** positively impacts sales
2. **Temperature**: Sales drop on colder days (10–15°C) compared to warmer days (20–30°C)
3. **Humidity**: Low humidity correlates with lower sales
4. **Activity Flag**: Promotions significantly increase sales
5. **Precipitation**: Minimal impact on sales
6. **Time of Day**: Higher sales in morning and afternoon
7. **Day of Week**: Weekends see more sales than weekdays

📈 Sample Visualizations
<div align="center">
  <img width="400" height="300" alt="Sales Analysis Visualization" src="https://github.com/user-attachments/assets/8ae01af5-2018-4f0e-8c3e-90a3aef321f7" />
  <img width="400" height="300" alt="Demand Forecast Visualization" src="https://github.com/user-attachments/assets/32e16d27-a981-48df-be7b-45874a3250b7" />
</div>
<img width="400" height="300" alt="EDA Analysis" src="https://github.com/user-attachments/assets/51606dc5-209a-4a8a-98aa-dc7ab930ce49" />
✅ Results
<img width="1919" height="900" alt="FreshRetailNet Results Dashboard" src="https://github.com/user-attachments/assets/e0f2c4ef-4a34-446c-b44d-f7b0643232f5" />


## ✅ Results

<img width="1919" height="900" alt="FreshRetailNet Results Dashboard" src="https://github.com/user-attachments/assets/e0f2c4ef-4a34-446c-b44d-f7b0643232f5" />

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Rajadurai-CSE/FreshRetailNet-50k-Forecast.git
cd FreshRetailNet-EndtoEnd
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launch the Streamlit App

```bash
cd streamlit-app
streamlit run app.py
```

## 🔮 Future Enhancements

- Experiment with **advanced strategies** for latent demand recovery
- Forecast at the **category level** instead of only SKU level
- Incorporate **deep learning models** (e.g., LSTMs, Transformers)
- Enhance app with **interactive model comparison and dashboards**

## 🙌 Acknowledgements

- **Dataset**: FreshRetailNet-50K
- **Libraries**: Pandas, Scikit-learn, XGBoost, LightGBM, Streamlit

---

✨ *Thank you for exploring this project!*
