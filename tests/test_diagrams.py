import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(PROJECT_ROOT)

from src.diagrams import plot_revenue_by_category


def main():
    # Ladda datan
    df = pd.read_csv("data/ecommerce_sales.csv")

    # Testa funktionen
    plot_revenue_by_category(df)

    # Visa diagrammet
    plt.show()

    input("Tryck Enter för att avsluta...")


if __name__ == "__main__":
    main()
