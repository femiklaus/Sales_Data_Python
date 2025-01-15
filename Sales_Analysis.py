import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Generate 200 lines of sales data
def generate_sales_data():
    np.random.seed(42)

    salespeople = ["Emeka", "Chioma", "Bola", "Ahmed", "Ngozi", "Adebayo", "Fatima", "Ifeanyi"]
    regions = ["North", "South", "East", "West"]
    states = ["Kano", "Lagos", "Anambra", "Kaduna", "Oyo", "Abia", "Sokoto", "Ekiti"]
    product_codes = [f"P{i:03d}" for i in range(1, 21)]
    product_names = [f"Product_{i}" for i in range(1, 21)]

    data = {
        "Salesperson": [random.choice(salespeople) for _ in range(200)],
        "Region": [random.choice(regions) for _ in range(200)],
        "State": [random.choice(states) for _ in range(200)],
        "Sales Quantity": np.random.randint(1, 50, 200),
        "Product Code": [random.choice(product_codes) for _ in range(200)],
        "Product Name": [random.choice(product_names) for _ in range(200)],
        "Price (Naira)": np.random.randint(500, 20000, 200),
        "Discount (%)": np.random.randint(0, 30, 200),
    }

    data["Total Sales (Naira)"] = [
        round(data["Sales Quantity"][i] * data["Price (Naira)"][i] * (1 - data["Discount (%)"][i] / 100), 2)
        for i in range(200)
    ]

    return pd.DataFrame(data)

# Generate and save data
data = generate_sales_data()
data.to_csv("sales_data.csv", index=False)

# Analyze and visualize data
def analyze_and_visualize(data):
    print("\nData Overview:\n", data.head())
    print("\nSummary Statistics:\n", data.describe())

    # Visualizations
    plt.figure(figsize=(16, 10))

    # 1. Sales by Region
    plt.subplot(2, 3, 1)
    sns.barplot(x="Region", y="Total Sales (Naira)", data=data, ci=None, estimator=sum, palette="viridis")
    plt.title("Total Sales by Region")
    plt.ylabel("Total Sales (Naira)")

    # 2. Sales by State
    plt.subplot(2, 3, 2)
    sns.barplot(x="State", y="Total Sales (Naira)", data=data, ci=None, estimator=sum, palette="magma")
    plt.xticks(rotation=45)
    plt.title("Total Sales by State")

    # 3. Salesperson Performance
    plt.subplot(2, 3, 3)
    sns.barplot(x="Salesperson", y="Total Sales (Naira)", data=data, ci=None, estimator=sum, palette="cubehelix")
    plt.title("Salesperson Performance")
    plt.ylabel("Total Sales (Naira)")

    # 4. Discount Distribution
    plt.subplot(2, 3, 4)
    sns.histplot(data["Discount (%)"], bins=10, kde=True, color="skyblue")
    plt.title("Discount Distribution")
    plt.xlabel("Discount (%)")

    # 5. Sales Quantity Distribution
    plt.subplot(2, 3, 5)
    sns.histplot(data["Sales Quantity"], bins=10, kde=True, color="coral")
    plt.title("Sales Quantity Distribution")
    plt.xlabel("Sales Quantity")

    # 6. Price Distribution
    plt.subplot(2, 3, 6)
    sns.boxplot(data["Price (Naira)"], color="lime")
    plt.title("Price Distribution")

    plt.tight_layout()
    plt.show()

# Run analysis and visualization
analyze_and_visualize(data)
