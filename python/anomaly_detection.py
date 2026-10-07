import pandas as pd

# Load retailer metrics
metrics = pd.read_csv("outputs/retailer_quality_metrics.csv")

# Columns to evaluate
cols = ["cancellation_rate", "reschedule_rate", "on_time_rate", "escalation_rate"]

# Outlier detection
for col in cols:
    mean = metrics[col].mean()
    std = metrics[col].std()
    metrics[f"{col}_is_outlier"] = (metrics[col] > mean + 2 * std).astype(int)

# Save output
metrics.to_csv("outputs/retailer_quality_anomalies.csv", index=False)
