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


def plot_revenue_over_time(df: pd.DataFrame, freq: str = "M"):
    """
    Linjediagram: intäkt över tid.
    
    freq:
        'D' = per dag
        'W' = per vecka
        'M' = per månad (standard)
    Använder kolumnerna 'date' och 'revenue'.
    """
    df_copy = df.copy()

    # Gör om date till datetime
    df_copy["date"] = pd.to_datetime(df_copy["date"])

    # Gruppera och summera intäkter per tidsenhet
    grouped = (
        df_copy
        .set_index("date")
        .groupby(pd.Grouper(freq=freq))["revenue"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    plt.figure()
    plt.plot(grouped["date"], grouped["revenue"], marker="o")
    plt.xlabel("Datum")
    plt.ylabel("Intäkt (revenue)")
    plt.title(f"Intäkt över tid (freq={freq})")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
