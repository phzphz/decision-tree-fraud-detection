"""Generate synthetic pipeline data; not real transactions or a benchmark."""
import csv
import random
from pathlib import Path

path = Path("DT.csv")
if path.exists():
    raise SystemExit("DT.csv already exists; refusing to overwrite it.")
rng = random.Random(42)
with path.open("w", newline="", encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow(["amount_scaled", "velocity", "account_age", "fraud"])
    for _ in range(300):
        amount, velocity, age = rng.random(), rng.random(), rng.random()
        label = int(amount + velocity - 0.3 * age + rng.uniform(-0.4, 0.4) > 1.0)
        writer.writerow([amount, velocity, age, label])
print("Wrote 300 SYNTHETIC rows to DT.csv. Metrics on this file are not real fraud-detection results.")
