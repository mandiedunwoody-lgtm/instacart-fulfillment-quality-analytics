import pandas as pd

metrics = pd.read_csv("outputs/retailer_quality_anomalies.csv")

insights = []

for _, row in metrics.iterrows():
    if row["cancellation_rate_is_outlier"] == 1:
        insights.append(
            f"Retailer {row['retailer_id']} shows a cancellation rate significantly above average."
        )
    if row["escalation_rate_is_outlier"] == 1:
        insights.append(
            f"Retailer {row['retailer_id']} has an elevated escalation rate, indicating potential operational issues."
        )

with open("outputs/retailer_insights.txt", "w") as f:
    for line in insights:
        f.write(line + "\n")
