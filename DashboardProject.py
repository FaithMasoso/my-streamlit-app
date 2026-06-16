import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Interactive Dashboard",
    layout="wide"
)

st.title("Interactive Dashboard")

df = pd.read_excel("sales_data.xlsx")
st.dataframe(df)
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[df["Region"].isin(region)]
total_sales = filtered_df["Sales"].sum()

avg_sales = filtered_df["Sales"].mean()

transactions = len(filtered_df)
col1,col2,col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Average Sales", f"${avg_sales:,.0f}")
col3.metric("Transactions", transactions)
region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig, use_container_width=True)
trend = filtered_df.groupby("Date")["Sales"].sum().reset_index()

fig2 = px.line(
    trend,
    x="Date",
    y="Sales",
    title="Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)
st.subheader("Detailed Data")

st.dataframe(filtered_df)
