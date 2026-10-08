# Instacart Fulfillment Quality & Retailer Performance Analytics

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Active-00C875?style=for-the-badge)
![Pages](https://img.shields.io/badge/Dashboard%20Pages-3-4A9EFF?style=for-the-badge)
![Last Updated](https://img.shields.io/badge/Updated-Oct%202026-FF6B35?style=for-the-badge)

> A production-grade Power BI dashboard for monitoring end-to-end fulfillment quality, retailer performance, and operational anomalies across the Instacart fulfillment network.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dashboard Pages](#dashboard-pages)
- [Key Metrics and KPIs](#key-metrics-and-kpis)
- [Data Model](#data-model)
- [DAX Measures](#dax-measures)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Insights Summary](#insights-summary)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## Project Overview

This Power BI dashboard provides real-time visibility into Instacart's fulfillment ecosystem - tracking order accuracy, delivery timeliness, retailer compliance, and anomaly patterns across regions and categories.

### Business Objectives

| Objective | Target | Current |
|-----------|--------|---------|
| On-Time Delivery Rate | >= 95% | 94.2% |
| Order Accuracy Rate | >= 98% | 97.8% |
| Avg Fulfillment Time | <= 40 min | 38.4 min |
| Substitution Rate | <= 7% | 8.3% |
| Active Retailer Score | >= 80/100 | 82.4/100 |

### Audience

- **Operations Leadership** - strategic KPI monitoring and anomaly response
- **Retailer Success Managers** - individual retailer performance coaching
- **Supply Chain Analysts** - trend analysis and forecasting
- **Product Teams** - substitution and accuracy improvement initiatives

---

## Dashboard Pages

### Page 1 - Fulfillment Quality Overview

| Visual | Type | Key Insight |
|--------|------|-------------|
| KPI Cards (x4) | Card | OTD Rate, Accuracy Rate, Avg Time, Sub Rate |
| On-Time Rate by Region | Horizontal Bar | South region 2.3% below network avg |
| Fulfillment Time Trend | Line Chart | 12-month declining trend - positive |
| Order Accuracy by Category | 100% Stacked Bar | Specialty has highest error rate (9%) |
| Substitution Rate Matrix | Conditional Table | Specialty x South hotspot at 18% |

**Slicers:** Date Range (Q1-Q3 2026) - Region - Retailer Category

### Page 2 - Retailer Performance and Anomalies

| Visual | Type | Key Insight |
|--------|------|-------------|
| KPI Cards (x4) | Card | Active Retailers, Avg Score, Anomalies, Top Score |
| Performance Scatter Plot | Scatter | 23 retailers in Critical quadrant |
| Anomaly Detection Timeline | Bar + Control Lines | UCL breached in Sep and Oct 2026 |
| Retailer Leaderboard | Sortable Table | 10 retailers flagged Watch or Critical |

### Page 3 - Insights and Recommendations

| Section | Content |
|---------|---------|
| Key Findings | 3 evidence-backed findings with impact ratings |
| Strategic Recommendations | 4 prioritized recommendations (P1/P2) with owners and timelines |
| Action Log | 6 tracked action items with status badges |

---

## Key Metrics and KPIs

```
On-Time Delivery Rate = Orders delivered on time / Total orders
Order Accuracy Rate   = Orders with no errors / Total orders
Avg Fulfillment Time  = Average(FulfillmentTimeMinutes) per order
Substitution Rate     = Total substitutions / Total items ordered
Retailer Score        = (0.4 x Fulfillment) + (0.35 x Accuracy) + (0.25 x Satisfaction) x 100
Anomaly UCL           = Network Mean + (2 x Standard Deviation)
```

---

## Data Model

Star schema with 2 fact tables and 3 dimension tables:

- **FactOrders** - OrderID, RetailerID, DateKey, RegionKey, FulfillmentTimeMinutes, IsOnTime, IsAccurate, SubstitutionCount, TotalItems
- **FactAnomalies** - AnomalyID, RetailerID, DateKey, AnomalyType, Severity
- **DimRetailer** - RetailerID, RetailerName, Category, Region, OnboardDate
- **DimDate** - DateKey, Date, Month, Quarter, Year, IsWeekend
- **DimRegion** - RegionKey, RegionName, State, Zone

| From Table | From Column | To Table | To Column | Cardinality |
|------------|-------------|----------|-----------|-------------|
| FactOrders | DateKey | DimDate | DateKey | Many-to-One |
| FactOrders | RetailerID | DimRetailer | RetailerID | Many-to-One |
| FactOrders | RegionKey | DimRegion | RegionKey | Many-to-One |
| FactAnomalies | DateKey | DimDate | DateKey | Many-to-One |
| FactAnomalies | RetailerID | DimRetailer | RetailerID | Many-to-One |

---

## DAX Measures

```dax
On-Time Delivery Rate =
DIVIDE(COUNTROWS(FILTER(FactOrders, FactOrders[IsOnTime] = 1)), COUNTROWS(FactOrders), 0)

Order Accuracy Rate =
DIVIDE(COUNTROWS(FILTER(FactOrders, FactOrders[IsAccurate] = 1)), COUNTROWS(FactOrders), 0)

Avg Fulfillment Time = AVERAGE(FactOrders[FulfillmentTimeMinutes])

Substitution Rate =
DIVIDE(SUM(FactOrders[SubstitutionCount]), SUM(FactOrders[TotalItems]), 0)

OTD Rate Prior Period =
CALCULATE([On-Time Delivery Rate], DATEADD(DimDate[Date], -1, MONTH))

Retailer Score =

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| BI Platform | Microsoft Power BI Desktop |
| Data Storage | Azure SQL Database / Instacart Analytics API |
| Data Refresh | Power BI Gateway (Scheduled - Daily at 6:00 AM ET) |
| Theme | Custom JSON Dark Theme (Instacart Navy #0F1B2D) |
| Version Control | GitHub |
| Prototype | Interactive HTML/Chart.js mockup |
| Documentation | Word DOCX Implementation Guide |

---

## Repository Structure

```
instacart-fulfillment-quality-analytics/
|
|-- assets/                                 # Banner and visual assets
|-- data/                                   # Source data files
|   |-- orders.csv
|   |-- retailers.csv
|   `-- sample-data/
|       |-- FactOrders_sample.csv
|       |-- FactAnomalies_sample.csv
|       |-- DimRetailer.csv
|       |-- DimDate.csv
|       `-- DimRegion.csv
|-- docs/
|   |-- implementation-guide.docx           # Full Power BI setup guide
|   |-- dax-measures.md                     # All DAX measures reference
|   `-- kpi-definitions.md                  # Metric definitions & thresholds
|-- notebooks/                              # Jupyter analysis notebooks
|-- outputs/                                # Generated reports and exports
|-- prototype/
|   `-- dashboard-prototype.html            # Interactive HTML mockup
|-- python/                                 # Python scripts
|-- screenshots/
|   |-- page1-fulfillment-quality.png
|   |-- page2-retailer-performance.png
|   `-- page3-insights-recommendations.png
|-- sql/                                    # SQL query files
|-- .gitignore
`-- README.md
```

---

## Getting Started

### Prerequisites

- Power BI Desktop (latest version) - [Download here](https://powerbi.microsoft.com/desktop)
- Access to Instacart Analytics data source (or use sample CSVs)
- Git installed locally

### Installation

```bash
git clone https://github.com/mandiedunwoody-lgtm/instacart-fulfillment-quality-analytics.git
cd instacart-fulfillment-quality-analytics
```

Then open `dashboard/InstacartFulfillmentDashboard.pbix` in Power BI Desktop.

### Apply the Custom Theme

1. Open the .pbix file in Power BI Desktop
2. Go to View > Themes > Browse for themes
3. Select `dashboard/instacart-dark-theme.json`
4. Click Apply

### Using Sample Data

1. Transform Data > New Source > Text/CSV
2. Load all files from `data/sample-data/`
3. Verify relationships match the schema diagram

---

## Insights Summary

Based on Q1-Q3 2026 data analysis:

### Critical Findings

1. **South Region On-Time Rate Gap** - The South region underperforms by **2.3 percentage points** vs. the network average, driven by last-mile logistics gaps in suburban delivery zones. Affects 22% of total order volume.

2. **Specialty Category Substitution Spike** - Substitution rates in the Specialty category increased **+4.1% QoQ**, correlating with SKU availability issues from 3 key suppliers. Customer NPS impact: -8 points.

3. **Anomaly Frequency Trend** - Anomaly frequency shows a statistically significant increasing trend (p < 0.05), with a **+23% month-over-month increase** in September-October 2026. UCL breached in the last 2 months.

### Strategic Recommendations

| Priority | Recommendation | Expected Impact | Timeline |
|----------|---------------|-----------------|----------|
| P1 | Optimize South Region Routing | +3.5% OTD rate | Q4 2026 |
| P1 | Supplier Diversification for Specialty SKUs | -40% substitution rate | Q4 2026 |
| P2 | Anomaly Early Warning System (48-hr alerts) | -60% response time | Q1 2027 |
| P2 | Retailer Performance Incentive Program | +15% retailer compliance | Q1 2027 |

---

## Roadmap

- [x] Data model design (star schema)
- [x] DAX measure library
- [x] Page 1: Fulfillment Quality Overview
- [x] Page 2: Retailer Performance & Anomalies
- [x] Page 3: Insights & Recommendations
- [x] Custom dark theme (Instacart branding)
- [x] Interactive HTML prototype
- [x] Implementation guide documentation
- [ ] Row-level security (RLS) by region
- [ ] Power BI Service deployment & scheduled refresh
- [ ] Mobile layout optimization
- [ ] Azure ML anomaly detection integration
- [ ] Automated email digest via Power Automate

---

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add: your feature description'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with Microsoft Power BI | Instacart Fulfillment Quality & Retailer Performance Analytics | October 2026
VAR FulfillmentWeight = 0.40
VAR AccuracyWeight = 0.35
VAR SatisfactionWeight = 0.25
RETURN ROUND(([On-Time Delivery Rate] * FulfillmentWeight + [Order Accuracy Rate] * AccuracyWeight + ([Avg Customer Satisfaction] / 5) * SatisfactionWeight) * 100, 1)

Anomaly UCL =
VAR MeanVal = AVERAGEX(VALUES(DimDate[Month]), CALCULATE(COUNTROWS(FactAnomalies)))
VAR StdDev = STDEV.P(FactAnomalies[AnomalyID])
RETURN MeanVal + (2 * StdDev)

OTD Rate Color =
SWITCH(TRUE(), [On-Time Delivery Rate] >= 0.95, "#00C875", [On-Time Delivery Rate] >= 0.90, "#FF6B35", "#FF4757")
```
