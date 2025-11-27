import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(PROJECT_ROOT)

from src.diagrams import (
    plot_revenue_by_category,
    plot_revenue_by_city
)


def main():
    df = pd.read_csv("data/ecommerce_sales.csv")

    # =====================================================
    # TEST 1 – intäkt per kategori
    # =====================================================
    print("\n==============================")
    print("TEST 1: plot_revenue_by_category")
    print("==============================\n")

    plot_revenue_by_category(df)
    plt.show()

    input("\nTryck Enter för att fortsätta till nästa test...")

    # =====================================================
    # TEST 2 – intäkt per stad
    # =====================================================
    print("\n==============================")
    print("TEST 2: plot_revenue_by_city")
    print("==============================\n")

    plot_revenue_by_city(df)
    plt.show()

    input("\nTryck Enter för att avsluta...")


if __name__ == "__main__":
    main()
