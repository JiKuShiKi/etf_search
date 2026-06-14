from tabulate import tabulate

def display_etf(etfs: list) -> None:
    """Zeigt einen oder mehrere ETFs als formatierte Tabelle."""
    kennzahlen = ["Name", "Ticker", "Währung", "Kurs", "Fondsvolumen", "TER", "Kategorie"]

    rows = []
    for kennzahl in kennzahlen:
        row = [kennzahl]
        for etf in etfs:
            if kennzahl == "Name":
                row.append(etf["name"])
            elif kennzahl == "Ticker":
                row.append(etf["ticker"])
            elif kennzahl == "Währung":
                row.append(etf["currency"])
            elif kennzahl == "Kurs":
                row.append(f"{etf['price']}€" if etf["price"] else "N/A")
            elif kennzahl == "Fondsvolumen":
                row.append(f"{etf['total_assets']:,}€" if etf["total_assets"] else "N/A")
            elif kennzahl == "TER":
                row.append(f"{etf['ter']*100:.2f}%" if etf["ter"] else "N/A")
            elif kennzahl == "Kategorie":
                row.append(etf["category"])
        rows.append(row)

    headers = ["Kennzahl"] + [etf["ticker"] for etf in etfs]
    print("\n")
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))