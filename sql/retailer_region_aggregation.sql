SELECT
    retailer_id,
    retailer_name,
    region,
    COUNT(*) AS total_orders,
    SUM(is_cancelled) AS cancelled_orders,
    SUM(is_rescheduled) AS rescheduled_orders,
    SUM(is_on_time) AS on_time_orders,
    AVG(order_value) AS avg_order_value
FROM flags
GROUP BY retailer_id, retailer_name, region;
