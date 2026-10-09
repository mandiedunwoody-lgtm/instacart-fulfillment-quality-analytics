# Instacart Fulfillment Quality & Retailer Performance Analytics

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Active-00C875?style=for-the-badge)
![Pages](https://img.shields.io/badge/Dashboard%20Pages-3-4A9EFF?style=for-the-badge)
![Last Updated](https://img.shields.io/badge/Updated-Oct%202026-FF6B35?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)
![Stack](https://img.shields.io/badge/Built%20With-Power%20BI%20%7C%20Azure%20SQL%20%7C%20Python-6a5acd?style=for-the-badge)

A production‑grade Power BI solution providing end‑to‑end visibility into Instacart’s fulfillment network — including delivery timeliness, order accuracy, retailer performance, and anomaly detection across regions and categories.

---

## Overview

This dashboard delivers real‑time operational insights across Instacart’s fulfillment ecosystem. It tracks:

- On‑time delivery performance  
- Order accuracy and error patterns  
- Retailer compliance and scoring  
- Substitution trends  
- Anomaly frequency and severity  

Designed for operations leadership, retailer success teams, supply chain analysts, and product teams focused on fulfillment quality.

### Business KPI Snapshot

| Objective | Target | Current |
|----------|--------|---------|
| On‑Time Delivery Rate | ≥ 95% | 94.2% |
| Order Accuracy Rate | ≥ 98% | 97.8% |
| Avg Fulfillment Time | ≤ 40 min | 38.4 min |
| Substitution Rate | ≤ 7% | 8.3% |
| Active Retailer Score | ≥ 80/100 | 82.4/100 |

---

## Dashboard Pages

### 1. Fulfillment Quality Overview

Key visuals:

- KPI cards (OTD, Accuracy, Avg Time, Sub Rate)  
- On‑Time Rate by Region  
- Fulfillment Time Trend (12‑month)  
- Order Accuracy by Category  
- Substitution Rate Matrix (Region × Category)

**Example insight:** South region OTD is **2.3 percentage points** below network average.

### 2. Retailer Performance & Anomalies

Key visuals:

- Retailer KPI cards  
- Performance scatter plot (quadrants)  
- Anomaly detection timeline (UCL breaches)  
- Retailer leaderboard with flags (Watch / Critical)

**Example insight:** 23 retailers fall into the **Critical** performance quadrant.

### 3. Insights & Recommendations

Summarizes:

- Key findings  
- Strategic recommendations (with priority and timelines)  
- Action log with status badges

---

## Data Model

Star schema with two fact tables and three dimensions:

- **FactOrders** — OrderID, RetailerID, DateKey, RegionKey, FulfillmentTimeMinutes, IsOnTime, IsAccurate, SubstitutionCount, TotalItems  
- **FactAnomalies** — AnomalyID, RetailerID, DateKey, AnomalyType, Severity  
- **DimRetailer** — RetailerID, RetailerName, Category, Region, OnboardDate  
- **DimDate** — DateKey, Date, Month, Quarter, Year, IsWeekend  
- **DimRegion** — RegionKey, RegionName, State, Zone  

Relationships:

- FactOrders → DimDate (Many‑to‑One)  
- FactOrders → DimRetailer (Many‑to‑One)  
- FactOrders → DimRegion (Many‑to‑One)  
- FactAnomalies → DimDate (Many‑to‑One)  
- FactAnomalies → DimRetailer (Many‑to‑One)

---

## Key Metrics & DAX

Core KPI definitions:

- **On‑Time Delivery Rate** = Orders delivered on time / Total orders  
- **Order Accuracy Rate** = Orders with no errors / Total orders  
- **Avg Fulfillment Time** = Average minutes per order  
- **Substitution Rate** = Total substitutions / Total items ordered  
- **Retailer Score** = weighted composite of fulfillment, accuracy, satisfaction  
- **Anomaly UCL** = Network mean + (2 × standard deviation)

These are implemented as DAX measures and used for KPI cards, conditional formatting, and anomaly detection.

---

## Tech Stack

| Component      | Technology                          |
|---------------|--------------------------------------|
| BI Platform   | Microsoft Power BI Desktop          |
| Data Storage  | Azure SQL Database / Instacart API  |
| Data Refresh  | Power BI Gateway (Daily 6:00 AM ET) |
| Theme         | Custom JSON Dark Theme (Instacart)  |
| Version Control | GitHub                            |
| Prototype     | HTML / Chart.js                     |
| Documentation | Word DOCX Implementation Guide      |

---

## Repository Structure

```text
instacart-fulfillment-quality-analytics/
│-- assets/
│-- data/
│   ├─ orders.csv
│   ├─ retailers.csv
│   └─ sample-data/
│       ├─ FactOrders_sample.csv
│       ├─ FactAnomalies_sample.csv
│       ├─ DimRetailer.csv
│       ├─ DimDate.csv
│       └─ DimRegion.csv
│-- docs/
│-- notebooks/
│-- outputs/
│-- prototype/
│-- python/
│-- screenshots/
│-- sql/
└-- README.md

```
## 🔍 Insights Summary

Based on Q1–Q3 2026 data:

### **Critical Findings**

1. **South Region On‑Time Delivery Gap**  
   - Underperforms by **2.3 percentage points** vs. the network average  
   - Driven by last‑mile logistics gaps in suburban delivery zones  
   - Impacts approximately **22%** of total order volume  

2. **Specialty Category Substitution Spike**  
   - Substitution rate increased **+4.1% QoQ**  
   - Correlates with SKU availability issues from three key suppliers  
   - Customer NPS impact: **−8 points**  

3. **Anomaly Frequency Trend**  
   - Statistically significant increasing trend (p < 0.05)  
   - **+23% month‑over‑month** increase in September–October 2026  
   - UCL breached in the last two months  

---

### **Strategic Recommendations**

| Priority | Recommendation                          | Expected Impact           | Timeline  |
|----------|------------------------------------------|---------------------------|-----------|
| **P1**   | Optimize South Region Routing            | +3.5% OTD rate            | Q4 2026   |
| **P1**   | Supplier Diversification for Specialty   | −40% substitution rate    | Q4 2026   |
| **P2**   | Anomaly Early Warning System (48‑hr)     | −60% response time        | Q1 2027   |
| **P2**   | Retailer Performance Incentive Program   | +15% retailer compliance  | Q1 2027   |
