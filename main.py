import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.search import search_etf
from src.display import display_etf

def main():
    """Hauptfunktion die alles zusammenbringt."""
    if len(sys.argv) < 2:
        print("Verwendung: python main.py <ticker>")
        print("Beispiel:   python main.py SXR8.DE")
        return
    query = sys.argv[1]
    print(f"Suche nach: {query}...")
    etf = search_etf(query)
    if etf:
        display_etf(etf)

if __name__ == "__main__":
    main()