# DashIQ — Data Model Design

## Objective
To define a structured data model for dashboard analysis using a star schema.

## Data Model Type
Star Schema

## Fact Table

### fact_sales
Contains transactional sales data and key metrics.

#### Columns:
- Order ID
- Order Date
- Ship Date
- Units Sold
- Unit Price
- Unit Cost
- Total Revenue
- Total Cost
- Total Profit
- Profit Margin

#### Foreign Keys:
- Region
- Country
- Item Type
- Sales Channel
- Order Priority
- Date

## Dimension Tables

### dim_date
- Date
- Year
- Month
- Quarter
- Month Name

### dim_region
- Region

### dim_country
- Country

### dim_product
- Item Type

### dim_channel
- Sales Channel

### dim_priority
- Order Priority

### dim_discount
- Discount Bucket

## Relationships

- dim_date → fact_sales (Order Date)
- dim_region → fact_sales (Region)
- dim_country → fact_sales (Country)
- dim_product → fact_sales (Item Type)
- dim_channel → fact_sales (Sales Channel)
- dim_priority → fact_sales (Order Priority)

## Model Validation

- Single fact table
- Clean dimension separation
- One-to-many relationships
- No circular dependencies

## Conclusion
The data model is optimized for dashboard performance, scalability, and ease of analysis.