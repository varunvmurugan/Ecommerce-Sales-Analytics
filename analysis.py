import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/superstore.csv")

# Clean column names (remove spaces)
df.columns = df.columns.str.strip()

print("Columns in dataset:")
print(df.columns)

# Convert Order Date to datetime (handle day-first format)
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Month'] = df['Order Date'].dt.month
    df['Year'] = df['Order Date'].dt.year

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# ---- SALES KPI ----
if 'Sales' in df.columns:
    total_sales = df['Sales'].sum()
    print("\nTotal Sales:", total_sales)
else:
    print("\n'Sales' column not found")

# ---- PROFIT KPI (if exists) ----
if 'Profit' in df.columns:
    total_profit = df['Profit'].sum()
    print("Total Profit:", total_profit)
else:
    print("'Profit' column not found in this dataset")

# ---- MONTHLY SALES TREND ----
if 'Month' in df.columns and 'Sales' in df.columns:
    monthly_sales = df.groupby('Month')['Sales'].sum()

    plt.figure()
    monthly_sales.plot(kind='line')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.show()
else:
    print("Cannot create monthly chart (Month or Sales missing)")
    # ---- TOP 5 PRODUCTS BY SALES ----
if 'Product Name' in df.columns and 'Sales' in df.columns:
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
    
    print("\nTop 5 Products by Sales:")
    print(top_products)

    plt.figure()
    top_products.plot(kind='bar')
    plt.title("Top 5 Products by Sales")
    plt.xlabel("Product Name")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Product Name column not found")
    # ---- CATEGORY WISE SALES ----
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

print("\nCategory Wise Sales:")
print(category_sales)

plt.figure()
category_sales.plot(kind='bar')
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
# ---- REGION WISE SALES ----
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

print("\nRegion Wise Sales:")
print(region_sales)

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
print("\n--- BUSINESS INSIGHTS ---")

print("1. The company generated total sales of $2.26 Million across all regions.")
print("2. Technology is the highest revenue-generating category, contributing the largest share of total sales.")
print("3. The West region outperforms all other regions, indicating strong market demand.")
print("4. The South region shows the lowest sales, suggesting potential growth opportunities.")
print("5. High-value products like Canon imageCLASS 2200 significantly drive revenue concentration.")
print("6. Monthly trends indicate seasonal fluctuations, useful for inventory planning.")