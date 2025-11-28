
import pandas as pd


# Funktion 1 – beräknar grundläggande nyckeltal
def compute_basic_metrics(df):
    total_revenue = df["revenue"].sum()
    total_units = df["units"].sum()
    n_orders = df["order_id"].nunique()
    aov = total_revenue / n_orders if n_orders else 0

    return total_revenue, total_units, n_orders, aov


# Funktion 2 – beräknar intäkt per kategori, stad eller annan grupp
def revenue_by_group(df, group_col):
    return (
        df.groupby(group_col)["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )



# Läs in data
df = pd.read_csv("data/ecommerce_sales.csv", parse_dates=["date"])

# 1. Grundläggande nyckeltal
total_revenue, total_units, n_orders, aov = compute_basic_metrics(df)

print("--------- Nyckeltal ---------")
print("Total intäkt:", total_revenue)
print("Totala antalet sålda enheter:", total_units)
print("Antal ordrar:", n_orders)
print("Average Order Value:", aov)
print()

# 2. Intäkt per kategori
print("--------- Intäkt per kategori ---------")
print(revenue_by_group(df, "category"))
print()

# 3. Intäkt per stad
print("--------- Intäkt per stad ---------")
print(revenue_by_group(df, "city"))
print()

# 4. Topp 3 kategorier
print("--------- Topp 3 kategorier ---------")
print(revenue_by_group(df, "category").head(3))
print()

