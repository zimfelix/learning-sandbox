import json
from pathlib import Path

# Locate the sample next to this script, regardless of the working directory.
data_path = Path(__file__).parent / "data" / "sample_usage.json"

with data_path.open(encoding="utf-8") as file:
    measurement = json.load(file)

print("Künstliche Beispieldaten – keine echte Abo-Nutzung")
print("Anbieter:", measurement["provider"])
print("Messzeitpunkt:", measurement["measured_at"])
print("Zeitraum:", measurement["reporting_period"])
print("API-Kostenäquivalent (USD):", measurement["api_equivalent_usd"])
