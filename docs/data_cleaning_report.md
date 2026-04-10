# DashIQ — Data Cleaning Report

## Dataset
sales_records.csv

## Objective
To transform the raw dataset into a clean and analysis-ready dataset.

---

## Cleaning Steps Performed

### 1. Duplicate Removal
- Identified duplicate rows
- Removed duplicates using Pandas

### 2. Missing Value Handling
- Checked missing values across all columns
- Dropped rows with critical missing fields
- Filled numeric values where appropriate

### 3. Text Standardization
- Cleaned text fields:
  - Item Type
  - Region
  - Country
  - Sales Channel
- Applied:
  - trimming spaces
  - consistent capitalization

### 4. Date Conversion
- Converted:
  - Order Date
  - Ship Date
- Ensured proper datetime format

### 5. Numeric Validation
- Converted numeric fields to correct types
- Checked for invalid or negative values

---

## Output
Clean dataset saved as:

data/processed/sales_records_clean.csv

---

## Conclusion
The dataset is now clean, consistent, and ready for analysis and dashboard development.