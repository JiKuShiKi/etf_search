from tabulate import tabulate

def display_etf(etf: dict) -> None:
    """Zeigt die ETF-Daten als formatierte Tabelle."""
    rows = [
        ["Name", etf["name"]],
        ["Ticker", etf["ticker"]],
        ["Währung", etf["currency"]],
        ["Kurs", f"{etf['price']}€" if etf["price"] else "N/A"],
        ["Fondsvolumen", f"{etf['total_assets']:,}€" if etf["total_assets"] else "N/A"],
        ["TER", f"{etf['ter'] * 100:.2f}%" if etf["ter"] else "N/A"],
        ["Kategorie", etf["category"]],
    ]
    print("\n")
    print(tabulate(rows, headers=["Kennzahl", "Wert"], tablefmt="rounded_outline"))