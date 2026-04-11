# DashIQ — Feature Engineering Notes

## Objective
To enhance the cleaned dataset by adding calculated columns for analysis and dashboarding.

---

## Engineered Columns

### 1. Year
Extracted from `Order Date` to enable yearly trend analysis.

### 2. Month
Numeric month extracted for sorting and grouping.

### 3. Quarter
Derived from `Order Date` to support quarterly reporting.

### 4. Order Month Name
Full month name (e.g., January) for better dashboard readability.

### 5. Profit Margin
Calculated as:
Total Profit / Total Revenue

Used to evaluate profitability.

### 6. Discount Bucket
Derived from Profit Margin (proxy logic):
- High Discount → Low margin
- Medium Discount → Moderate margin
- Low Discount → High margin

---

## Output
Enhanced dataset saved as:

../data/cleaned/sales_records_enhanced.csv

---

## Conclusion
The dataset now includes time-based and business metrics required for advanced analysis and dashboard visualization.