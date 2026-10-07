import pandas as pd

# Load data
orders = pd.read_csv("data/orders.csv", parse_dates=["order_date", "promised_delivery_time", "actual_delivery_time"])
retailers = pd.read_csv("data/retailers.csv", parse_dates=["launch_date"])
escalations = pd.read_csv("data/escalations.csv", parse_dates=["created_at", "resolved_at"])

# Fulfillment flags
orders["is_cancelled"] = (orders["status"] == "cancelled").astype(int)
orders["is_rescheduled"] = (orders["status"] == "rescheduled").astype(int)
orders["is_completed"] = (orders["status"] == "completed").astype(int)
orders["is_on_time"] = (
    (orders["status"] == "completed") &
    (orders["actual_delivery_time"] <= orders["promised_delivery_time"])
).astype(int)

# Retailer-level aggregation
retailer_metrics = (
    orders
    .groupby("retailer_id")
    .agg(
        total_orders=("order_id", "count"),
        cancelled_orders=("is_cancelled", "sum"),
        rescheduled_orders=("is_rescheduled", "sum"),
        completed_orders=("is_completed", "sum"),
        on_time_orders=("is_on_time", "sum"),
        avg_order_value=("order_value", "mean")
    )
)

# KPI calculations
retailer_metrics["cancellation_rate"] = retailer_metrics["cancelled_orders"] / retailer_metrics["total_orders"]
retailer_metrics["reschedule_rate"] = retailer_metrics["rescheduled_orders"] / retailer_metrics["total_orders"]
retailer_metrics["on_time_rate"] = retailer_metrics["on_time_orders"] / retailer_metrics["completed_orders"]

# Join retailer attributes
retailer_metrics = retailer_metrics.merge(retailers, on="retailer_id", how="left")

# Escalation counts
escalation_counts = (
    escalations
    .groupby("retailer_id")
    .agg(escalation_count=("escalation_id", "count"))
)

retailer_metrics = retailer_metrics.merge(escalation_counts, on="retailer_id", how="left").fillna({"escalation_count": 0})
retailer_metrics["escalation_rate"] = retailer_metrics["escalation_count"] / retailer_metrics["total_orders"]

# Save output
retailer_metrics.to_csv("outputs/retailer_quality_metrics.csv", index=True)
