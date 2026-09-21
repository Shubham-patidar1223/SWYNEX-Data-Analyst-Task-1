import pandas as pd

df = pd.read_csv("marketing_campaign.txt", sep="\t")

print(df.head())


# Dataset ka size
print("Dataset Shape:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)


# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records check
duplicates = df.duplicated().sum()

print("\nDuplicate Records:", duplicates)

# Check data types
print("\nData Types:")
print(df.dtypes)

print("\nMarital Status Values:")
print(df["Marital_Status"].value_counts())

print("\nEducation Values:")
print(df["Education"].value_counts())

print("\nCustomer Date Sample:")
print(df["Dt_Customer"].head(10))

print("\nDt_Customer Data Type:")
print(df["Dt_Customer"].dtype)

# Convert Dt_Customer into proper date format
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    format="%d-%m-%Y"
)

print("\nDt_Customer after conversion:")
print(df["Dt_Customer"].head())

print("\nNew Data Type:")
print(df["Dt_Customer"].dtype)

print("\nMissing Income:")
print(df["Income"].isnull().sum())

# Fill missing Income values with median
median_income = df["Income"].median()

df["Income"] = df["Income"].fillna(median_income)

print("\nMissing Income after cleaning:")
print(df["Income"].isnull().sum())

# Final duplicate check
print("\nDuplicate Records after Cleaning:")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_csv("marketing_campaign_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Final validation
print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

import pandas as pd

# ==========================================
# SWYNEX Technologies - Task 1
# Data Cleaning
# ==========================================

# 1. Load dataset
df = pd.read_csv("marketing_campaign.txt", sep="\t")

print("Original Dataset Shape:", df.shape)

# 2. View first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Column names
print("\nColumn Names:")
print(df.columns.tolist())

# 4. Data types
print("\nData Types:")
print(df.dtypes)

# 5. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 7. Check Marital Status values
print("\nMarital Status Values:")
print(df["Marital_Status"].value_counts())

# 8. Check Education values
print("\nEducation Values:")
print(df["Education"].value_counts())

# 9. Convert Dt_Customer to proper date format
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    format="%d-%m-%Y"
)

print("\nDt_Customer Data Type After Conversion:")
print(df["Dt_Customer"].dtype)

# 10. Fill missing Income values using median
median_income = df["Income"].median()
df["Income"] = df["Income"].fillna(median_income)

print("\nMissing Income After Cleaning:")
print(df["Income"].isnull().sum())

# 11. Final duplicate check
print("\nFinal Duplicate Records:")
print(df.duplicated().sum())

# 12. Final missing-value check
print("\nTotal Missing Values After Cleaning:")
print(df.isnull().sum().sum())

# 13. Save cleaned dataset
df.to_csv("marketing_campaign_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final Dataset Shape:", df.shape)