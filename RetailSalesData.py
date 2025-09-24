# Retail Sales Data Analysis - Starter Notebook

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv", parse_dates=["Order Date"])

# Preview data
print(df.head())

# -----------------------------
# Basic Info
# -----------------------------
print(df.info())
print(df.describe())

# -----------------------------
# 1. Total Sales & Profit Overview
# -----------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_order_value = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Order Value:", avg_order_value)

# -----------------------------
# 2. Monthly Sales Trend
# -----------------------------
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 3. Top 10 Products by Sales
# -----------------------------
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

# -----------------------------
# 4. Sales by Category
# -----------------------------
plt.figure(figsize=(6,6))
df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%.1f%%", startangle=90, colormap="Set3")
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()

# -----------------------------
# 5. Regional Sales Comparison
# -----------------------------
plt.figure(figsize=(8,6))
sns.barplot(x="Region", y="Sales", data=df, estimator=sum, ci=None, palette="magma")
plt.title("Sales by Region")
plt.show()

# -----------------------------
# Insights Example
# -----------------------------
print("\n--- Business Insights ---")
print("1. Top-selling product:", top_products.index[0])
print("2. Highest sales month:", monthly_sales.idxmax())
print("3. Category with highest sales:", df.groupby('Category')['Sales'].sum().idxmax())
