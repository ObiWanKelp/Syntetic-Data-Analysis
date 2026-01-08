import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Synthetic_Cleaned.csv")

#Revenue by Membersip Tier
grouped_top = df.groupby("membership")['purchase_amount'].sum().sort_values(ascending=False)
#Avg spend per Membership Tier
grouped_mean = df.groupby("membership")["purchase_amount"].mean()


#Revenue by Membersip Tier Plot
plt.figure()
grouped_top.plot(kind='bar',color='skyblue',edgecolor='black')
plt.title('Revenue by Membership')
plt.xlabel('Membership Tier')
plt.ylabel('Revenue')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Avg spend per Membership Tier Plot
plt.figure()
grouped_mean.plot(kind='bar',color='skyblue',edgecolor='black')
plt.title('Average Spend per Membership Tier')
plt.xlabel('Membership Tier')
plt.ylabel('Revenue')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Top 10% user contribution to revenue
user_rev = df.groupby('user_id')['purchase_amount'].sum()
user_rev_sorted = user_rev.sort_values(ascending=False)
top_n = int(len(user_rev_sorted)*0.10)
top_users = user_rev_sorted.head(top_n)

# Take the top 20 users
top20 = top_users.head(20)

plt.figure(figsize=(8,8))
plt.pie(
    top20, 
    labels=top20.index,        
    autopct="%1.1f%%",         
    startangle=90,             
    counterclock=False
)

plt.title("Revenue Share of Top 20 Users")
plt.show()

#Active vs Inactive
activity_status = df['active'].value_counts()
print(activity_status)

plt.figure(figsize=(6,6))
plt.pie(
    activity_status,
    labels=["Active Users", "Inactive Users"],  
    autopct="%1.1f%%",                          
    colors=["green", "red"],
    startangle=90
)

plt.title("Active vs Inactive Users")
plt.show()


