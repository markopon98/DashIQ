import streamlit as st
import pandas as pd
import sqlite3

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="DashIQ Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("data/cleaned/dashiq.db")
    df = pd.read_sql("SELECT * FROM fact_sales", conn)
    conn.close()
    return df

df = load_data()

# -----------------------------
# HEADER
# -----------------------------
st.title("📊 DashIQ — Sales Dashboard")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")
# Year filter
years = sorted(df["Year"].dropna().unique())
selected_year = st.sidebar.multiselect(
    "Select Year",
    options=years,
    default=years
)
regions = sorted(df["Region"].dropna().unique())
selected_region = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions
)
categories = sorted(df["Item Type"].dropna().unique())
selected_category = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)   
products = sorted(df["Item Type"].dropna().unique())
selected_product = st.sidebar.multiselect(
    "Select Product",
    options=products,
    default=products
)
filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Region"].isin(selected_region)) &
    (df["Item Type"].isin(selected_category)) &
    (df["Item Type"].isin(selected_product))
]
# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

total_revenue = filtered_df["Total Revenue"].sum()
total_profit = filtered_df["Total Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
profit_margin = total_profit / total_revenue

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("Margin", f"{profit_margin:.2%}")

# -----------------------------
# SAMPLE TABLE
# -----------------------------
st.subheader("Sample Data")
st.dataframe(df.head())