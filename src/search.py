import yfinance as yf
import pandas as pd

def search_etf(query: str) -> dict | None:
    """searching an ETF from yfinance based on name or ticker"""
    try:
        etf = yf.Ticker(query)
        info = etf.info
        fast = etf.fast_info
        if not info or "shortName" not in info:
            print(f"Kein ETF gefunden für: {query}")
            return None
        return {
            "name": info.get("shortName", "Unbekannt"),
            "ticker": query.upper(),
            "currency": info.get("currency", "N/A"),
            "price": round(fast["last_price"], 2) if fast else None,
            "total_assets": fast.get("market_cap", None) if fast else None,
            "ter": info.get("annualReportExpenseRatio", None),
            "category": info.get("category", "N/A"),
        }
    except Exception as e:
        print(f"Fehler bei der Suche nach {query}: {e}")
        return None