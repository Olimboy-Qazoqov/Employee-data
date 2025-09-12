# 📊 Full Python EDA for Retail Sales Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("Cleaned_employee_dataset.csv")

# -----------------------------
# 2. General Overview
# -----------------------------
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Stats:\n", df.describe(include="all"))

# -----------------------------
# 3. Univariate Analysis
# -----------------------------
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(exclude=np.number).columns

# Bar plots for categorical columns (Top 10 values)
for col in cat_cols:
    plt.figure(figsize=(10, 4))
    df[col].value_counts().head(10).plot(kind='bar')
    plt.title(f"Top 10 categories in {col}")
    plt.xticks(rotation=45)
    plt.show()

# -----------------------------
# 4. Bivariate Analysis
# -----------------------------
# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Scatter: Sales vs Quantity (if exist)
if "Sales" in df.columns and "Quantity" in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x="Quantity", y="Sales")
    plt.title("Sales vs Quantity")
    plt.show()

# -----------------------------
# 5. Time Series Analysis
# -----------------------------
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    
    # Monthly revenue trend
    monthly_sales = df.resample("M")["Sales"].sum()
    plt.figure(figsize=(12,6))
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.show()

    # Daily average sales (seasonality)
    df.groupby(df.index.dayofweek)["Sales"].mean().plot(kind="bar")
    plt.title("Average Sales by Day of Week (0=Mon, 6=Sun)")
    plt.show()

# -----------------------------
# 6. Customer & Product Insights
# -----------------------------
if "CustomerID" in df.columns:
    top_customers = df.groupby("CustomerID")["Sales"].sum().sort_values(ascending=False).head(10)
    top_customers.plot(kind="bar", figsize=(10,5))
    plt.title("Top 10 Customers by Revenue")
    plt.show()

if "Product" in df.columns:
    top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
    top_products.plot(kind="bar", figsize=(10,5))
    plt.title("Top 10 Products by Revenue")
    plt.show()

# -----------------------------
# 7. Outlier Detection
# -----------------------------
if "Sales" in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df["Sales"])
    plt.title("Outliers in Sales")
    plt.show()

    # Detect top 5 highest transactions
    print("\nTop 5 Outlier Transactions:\n", df.nlargest(5, "Sales"))
