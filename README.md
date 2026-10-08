# Instacart Fulfillment Quality & Retailer Performance Analytics

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboards-yellow?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Documentation-lightgrey?style=for-the-badge)

## Overview

This project simulates the type of work done by a Data Analyst on Instacart's Platform Excellence Ops (PEO) Analytics team. It focuses on:

- Fulfillment quality metrics (cancellations, reschedules, timeliness)
- Retailer performance monitoring
- Anomaly detection and root-cause analysis
- Proactive performance tracking and escalation support
- Clear, stakeholder-ready insights and narratives

The goal is to demonstrate an end-to-end analytics workflow:
1. Data design and ingestion
2. Cleaning, validation, and reconciliation
3. Metric definition and calculation
4. Anomaly detection and performance fluctuation analysis
5. Insight generation and recommendations

---

## Data Model

### 1. `orders.csv`

**Columns:**
- `order_id` (string)
- `order_date` (date)
- `retailer_id` (string)
- `region` (string)
- `promised_delivery_time` (datetime)
- `actual_delivery_time` (datetime)
- `status` (string: `completed`, `cancelled`, `rescheduled`)
- `cancellation_reason` (string, nullable)
- `reschedule_reason` (string, nullable)
- `basket_size` (numeric)
- `order_value` (numeric)
- `shopper_id` (string)

### 2. `retailers.csv`

**Columns:**
- `retailer_id` (string)
- `retailer_name` (string)
- `region` (string)
- `launch_date` (date)
- `tier` (string: `strategic`, `core`, `long_tail`)

### 3. `escalations.csv`

**Columns:**
- `escalation_id` (string)
- `order_id` (string)
- `retailer_id` (string)
- `created_at` (datetime)
- `escalation_type` (string: `timeliness`, `cancellation`, `reschedule`, `substitution`, `other`)
- `severity` (string: `low`, `medium`, `high`)
- `resolved_at` (datetime, nullable)

---

## Key Metrics

### Fulfillment Quality Metrics

- **Cancellation Rate**
  

\[
  \text{Cancellation Rate} = \frac{\text{Cancelled Orders}}{\text{Total Orders}}
  \]



- **Reschedule Rate**
  

\[
  \text{Reschedule Rate} = \frac{\text{Rescheduled Orders}}{\text{Total Orders}}
  \]



- **On-Time Delivery Rate**
  

\[
  \text{On-Time Rate} = \frac{\text{Orders Delivered On or Before Promised Time}}{\text{Completed Orders}}
  \]



- **Escalation Rate**
  

\[
  \text{Escalation Rate} = \frac{\text{Orders with Escalations}}{\text{Total Orders}}
  \]



### Retailer Performance Metrics

- Metrics calculated **per retailer** and **per region**:
  - Cancellation rate
  - Reschedule rate
  - On-time delivery rate
  - Escalation rate
  - Average order value
  - Basket size distribution

---

## SQL Workflow (Outline)

File: `sql/retailer_quality_metrics.sql`

1. **Join orders and retailers**

```sql
WITH base AS (
    SELECT
        o.order_id,
        o.order_date,
        o.retailer_id,
        r.retailer_name,
        r.region,
        o.status,
        o.promised_delivery_time,
        o.actual_delivery_time,
        o.order_value
    FROM orders o
    JOIN retailers r
        ON o.retailer_id = r.retailer_id
)
