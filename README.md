---
# Synthetic User Data Cleaning with Pandas

This project demonstrates an end-to-end data cleaning and preprocessing pipeline using Pandas on a synthetic but realistic user dataset.

The dataset is intentionally messy and contains common real-world data quality issues such as missing values, inconsistent categorical labels, invalid numeric values, mixed date formats, and duplicate records.

The current focus of this project is **data cleaning only**. Analysis and visualization will be added in a later stage.
---

## Folder Structure

```
SyntheticAnalysis/
│
├── dirty_user_data.csv        # Raw synthetic dataset
├── Synthetic_Cleaning.py      # Data cleaning & preprocessing script
├── Synthetic_Analysing.py     # Data analysis / EDA script 
└── Synthetic_Cleaned.csv      #Synthetic_Cleaned.csv 

```

---

## Dataset Description

The dataset represents user profile and transaction data from a hypothetical consumer application.

Columns include:

- user_id
- name
- age
- gender
- city
- signup_date
- purchase_amount
- membership
- active

---

## Cleaning Steps Implemented

- Replaced fake and inconsistent missing values with NaN
- Handled invalid numeric entries such as unrealistic ages and negative purchase values
- Normalized categorical string columns for consistent casing and formatting
- Parsed mixed-format date values safely
- Removed duplicate users using business keys
- Performed controlled missing value imputation using sentinel values
- Calculated missing value percentages prior to imputation

---

## Design Decisions

- Cleaning logic is applied at the row level using explicit `.loc` operations
- Group-based operations are used only where contextual information is required
- Sentinel values are used deliberately to preserve row counts for downstream analysis
- Data types are kept explicit and stable to avoid silent casting issues

---

## Usage

Run the cleaning script from this directory:

```bash
python Synthetic_Cleaning.py
```

The script reads the raw CSV, applies cleaning steps, and prepares the dataset for future analysis and dashboarding.

---

## Doing Exploratory Data Analysis

- Built a few plots while analysing the data
- Created visualizations using Matplotlib

---

## What next 

- Build an interactive dashboard on top of the cleaned dataset
- Analyse more data from this dataset

---

## Notes

This project uses synthetic data created for learning and demonstration purposes.

---
