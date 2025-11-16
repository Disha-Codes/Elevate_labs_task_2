import pandas as pd
import numpy as np

# 1. LOAD THE DATA
df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")


# 2. CLEAN COLUMN NAMES
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")


# 3. FIX ENCODING ISSUES & STRIP TEXT
text_cols = df.select_dtypes(include=["object"]).columns

for col in text_cols:
    df[col] = df[col].astype(str).str.replace("\xa0", " ", regex=False)
    df[col] = df[col].str.strip()
    df[col] = df[col].str.replace(r"\s+", " ", regex=True)


# 4. CONVERT DATE COLUMNS
date_cols = ["Order_Date", "Ship_Date"]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")


# 5. POSTAL CODE CLEANING
df["Postal_Code"] = df["Postal_Code"].astype("Int64").astype(str)
df["Postal_Code"] = df["Postal_Code"].str.replace(".0", "", regex=False)


# 6. REMOVE DUPLICATES
df.drop_duplicates(inplace=True)


# 7. EXPORT CLEAN FILE
df.to_csv("cleaned_superstore.csv", index=False)

print("Cleaning complete! File saved as cleaned_superstore.csv")
