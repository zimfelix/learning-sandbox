import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


def main():
    data_path = PROJECT_DIR / "data" / "sample_usage.json"
    with data_path.open(encoding="utf-8") as file:
        measurement = json.load(file)

    print("Künstliche Beispieldaten – keine echte Abo-Nutzung")
    print("Anbieter:", measurement["provider"])
    print("Messzeitpunkt:", measurement["measured_at"])
    print("Zeitraum:", measurement["reporting_period"])
    print("API-Kostenäquivalent (USD):", measurement["api_equivalent_usd"])


if __name__ == "__main__":
    main()
