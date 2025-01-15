import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pre-generated data from a CSV file
data = pd.read_csv("sales_data.csv")

# Analyze and visualize the data
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
