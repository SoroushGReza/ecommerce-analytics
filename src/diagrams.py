import pandas as pd
import matplotlib.pyplot as plt


def plot_revenue_by_category(df: pd.DataFrame):
    """
    Stapeldiagram: intäkt per kategori.
    Använder kolumner 'category' och 'revenue'.
    """
    grouped = (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    plt.figure()
    plt.bar(grouped["category"], grouped["revenue"])
    plt.xlabel("Kategori")
    plt.ylabel("Intäkt (revenue)")
    plt.title("Intäkt per kategori")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    
def plot_revenue_by_city(df: pd.DataFrame):
    """
    Stapeldiagram: intäkt per stad.
    Använder kolumnerna 'city' och 'revenue'.
    """
    grouped = (
        df.groupby("city", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    plt.figure()
    plt.bar(grouped["city"], grouped["revenue"])
    plt.xlabel("Stad")
    plt.ylabel("Intäkt (revenue)")
    plt.title("Intäkt per stad")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

