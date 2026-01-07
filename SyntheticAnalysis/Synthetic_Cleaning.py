import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)
df = pd.read_csv('python1/PandasPrac/SyntheticAnalysis/dirty_user_data.csv')
print(df)


#Cleaned fake missing
fake_missing = [
    "NA", "N/A", "null", "NULL", "None",
    "", " ", "-", "?",
    "Unknown", "UNKNOWN", "unknown",
    "ERROR", "Error", "error", "nan","invalid_date"
]
df = df.replace(fake_missing,np.nan)

#Cleaned the age column
df.loc[df['age']>100,'age'] = np.nan
df['age'] = df['age'].fillna(df['age'].median())

#Normalised string columns(case)
str_cols = ['name','gender','city','membership']
for col in str_cols:
    df[col] = df[col].str.strip().str.lower()
    df[col] = df[col].str.title()

#Normalised gender column
df['gender'] = df['gender'].replace({'Male':'M','Female':'F'})

#Normalised purchase_amount
df['purchase_amount'] = pd.to_numeric(df['purchase_amount'])
df.loc[df['purchase_amount']<=0,'purchase_amount'] = np.nan

#Normalised dates
df['signup_date'] = pd.to_datetime(df['signup_date'],errors='coerce',format='mixed',dayfirst=True)

#Removing duplicates
df = df.drop_duplicates(subset=['user_id'])


# -------------------------------
# MISSING % BEFORE FILLING
# -------------------------------
missing_pct_before = (df.isnull().mean() * 100).round(2)
total_missing_before = round(df.isnull().sum().sum() / df.size * 100, 2)

print("\nMissing % per column BEFORE filling:")
print(missing_pct_before)


#Fixing Missing
df = df.fillna({
    'age': -1,                       
    'city': 'Unknown City',
    'signup_date': pd.NaT,           
    'purchase_amount': 0,
    'membership': 'Unknown',
    'active': False,
    'name':'Unknown Name',
    'gender':'Unknown Gender'
})

#Sort by spent
df = df.sort_values('purchase_amount',ascending=False)
