# %% [markdown]
# # Fuel Usage & KOKO Awareness Analysis – Kisumu County
# _By Ian Mutunga – July 2025_

# %% [markdown]
# ## 1. Introduction
# KOKO Networks is exploring market entry into Kisumu County with its clean fuel solution. This notebook documents the full analysis conducted on simulated data representing 101 households. The objective is to assess fuel usage behavior, price sensitivity, income levels, and awareness of KOKO products.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# %% [markdown]
# ## 2. Load and Inspect Data

# %%
# Load cleaned data
file_path = r"C:\Users\PC\Downloads\Untitled spreadsheet (1).xlsx"
df = pd.read_excel(file_path, sheet_name='Sheet1')
df.columns = [col.strip().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_') for col in df.columns]
df.head()

# %% [markdown]
# ## 3. Data Cleaning Summary

# %%
# Convert columns to numeric
df['Monthly_Income_KES'] = pd.to_numeric(df['Monthly_Income_KES'], errors='coerce')
df['Preferred_Fuel_Cost_KES_month'] = pd.to_numeric(df['Preferred_Fuel_Cost_KES_month'], errors='coerce')
df['Price_Sensitivity_1-5'] = pd.to_numeric(df['Price_Sensitivity_1-5'], errors='coerce')
df.info()

# %% [markdown]
# ## 4. Descriptive Statistics

# %%
# Summary of numeric columns
df[['Monthly_Income_KES', 'Price_Sensitivity_1-5', 'Preferred_Fuel_Cost_KES_month']].describe()

# %% [markdown]
# ## 5. Categorical Frequency Distributions

# %%
df['Location'].value_counts(), df['Primary_Fuel'].value_counts(), df['Aware_of_KOKO_Yes_No'].value_counts(), df['Not_interested_in_KOKO_Yes_No'].value_counts()

# %% [markdown]
# ## 6. Visualizations

# %%
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Location', hue='Primary_Fuel')
plt.title('Primary Fuel Use by Neighborhood')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Aware_of_KOKO_Yes_No', hue='Not_interested_in_KOKO_Yes_No')
plt.title('KOKO Awareness vs Interest')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(7, 4))
sns.histplot(df['Price_Sensitivity_1-5'].dropna(), bins=5)
plt.title('Price Sensitivity Distribution')
plt.tight_layout()
plt.show()

# %%
# Apply winsorizattion
from scipy.stats.mstats import winsorize

df['Monthly_Income_Winsorized'] = winsorize(df['Monthly_Income_KES'], limits=[0.05, 0.05])
sns.histplot(df['Monthly_Income_Winsorized'], bins=30)

plt.figure(figsize=(8, 5))
sns.histplot(df['Monthly_Income_KES'], bins=30)
plt.title('Monthly Income Distribution')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Monthly_Income_KES', y='Preferred_Fuel_Cost_KES_month', data=df)
plt.title('Income vs Preferred Fuel Spend')
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 7. Correlation Analysis

# %%
corr = df[['Monthly_Income_KES', 'Preferred_Fuel_Cost_KES_month']].corr()
corr


