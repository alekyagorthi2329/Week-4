# Complete Data Analysis Project
# E-commerce Sales Analysis

import os
import pandas as pd
import matplotlib.pyplot as plt

# Create visualization folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
try:
    df = pd.read_csv("data/sales_data.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: sales_data.csv not found.")
    exit()

# -----------------------------
# Explore Dataset
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Clean Dataset
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# -----------------------------
# Basic Analysis
# -----------------------------

total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()

print("\n===== SALES SUMMARY =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Sale: ${average_sales:,.2f}")
print(f"Highest Sale: ${highest_sale:,.2f}")

# Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum()

best_product = product_sales.idxmax()

print(f"Best Selling Product: {best_product}")

# -----------------------------
# Chart 1 - Bar Chart
# -----------------------------

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# -----------------------------
# Chart 2 - Line Chart
# -----------------------------

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"].sum()

    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("visualizations/monthly_sales.png")
    plt.close()

print("\nCharts saved inside the visualizations folder.")