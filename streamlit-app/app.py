import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data_transformation import get_processed_data
from src.model_selection import time_series_split, train_and_select_model
from src.model_selection import save_model, load_model, create_features

# ---------------------------------------------------------
# Load processed data once (fast reloads for Streamlit)
@st.cache_data
def load_data():
    return get_processed_data()

df = load_data()

# ---------------------------------------------------------
# Sidebar Inputs
st.sidebar.header("Sales Forecast Settings")

# Store selection
store_ids = df["store_id"].unique().tolist()
store_id = st.sidebar.selectbox("Select Store", sorted(store_ids))

# Product selection (filtered by store)
products = df[df["store_id"] == store_id]["product_id"].unique().tolist()
product_id = st.sidebar.selectbox("Select Product", sorted(products))

# Training & forecast windows
train_days = st.sidebar.slider("Training Window (days)", 10, len(df[(df["store_id"] == store_id) & (df["product_id"]==product_id)]), step=1)


if st.sidebar.button("Run Forecast"):

    df_subset = df[(df["store_id"] == store_id) & (df["product_id"] == product_id)]
    df_subset = df_subset.sort_values("dt").reset_index(drop=True)

    # 🔍 Try loading cached model
    best_model = load_model(store_id, product_id, train_days)

    if best_model:
        st.success("Loaded cached model 🚀")
        results = {"cached_model": {"rmse": "N/A", "mae": "N/A"}}  # placeholder metrics
    else:
        st.info("Training new model ⚡")
        train, val = time_series_split(df_subset, train_days)
        best_model, results = train_and_select_model(train, val)
        save_model(best_model, store_id, product_id, train_days)

    # Show best model info
    if results and results != {"cached_model": {"rmse": "N/A", "mae": "N/A"}}:
        best_model_name = min(results, key=lambda k: results[k]['rmse'])
        best_model_metrics = results[best_model_name]
        st.subheader("Best Model")
        st.write(f"Model: {best_model_name}")
        st.write(best_model_metrics)

    # Forecast on validation window
    val_feat = create_features(df_subset.iloc[train_days:])  # last window
    X_val = val_feat.drop(columns=["sale_amount", "dt"])
    y_val = val_feat["sale_amount"]

    print(val_feat)
    preds = best_model.predict(X_val)

    # Plot results
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(val_feat["dt"], y_val, label="Actual Sales", marker="o")
    ax.plot(val_feat["dt"], preds, label="Forecast", marker="x")
    ax.set_title(f"Store {store_id} - Product {product_id}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales Amount")
    ax.legend()

    st.pyplot(fig)

    # Show evaluation metrics
    st.subheader("Model Evaluation")
    st.write(results)
