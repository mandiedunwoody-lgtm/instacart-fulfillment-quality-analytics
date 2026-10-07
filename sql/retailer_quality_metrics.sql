, flags AS (
    SELECT
        *,
        CASE
            WHEN status = 'cancelled' THEN 1 ELSE 0
        END AS is_cancelled,
        CASE
            WHEN status = 'rescheduled' THEN 1 ELSE 0
        END AS is_rescheduled,
        CASE
            WHEN status = 'completed'
                 AND actual_delivery_time <= promised_delivery_time
            THEN 1 ELSE 0
        END AS is_on_time
    FROM base
)
