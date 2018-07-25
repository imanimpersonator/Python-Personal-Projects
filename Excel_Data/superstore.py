# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import time as time


start = time.time()

# Reads excel file in external_files. Refer to file to see columns


df = pd.read_excel("external_files/Superstore.xls")

df.head()

# Counts how many Order ID's start with CA
totca = sum(df["Order ID"].apply(lambda x: x.split("-")[0]) == "CA")

# Same as above, but with "US" Prefix
totus = sum(df["Order ID"].apply(lambda x: x.split("-")[0]) == "US")

# Finds all customers with First name that starts with "S"
snames = df[df["Customer Name"].apply(lambda x: x.startswith("S"))]


# simple pivot table
pt = pd.pivot_table(df, index = "Customer Name")

pt2 = pd.pivot_table(snames, index = "Customer Name")

# counts data entries of customers who's first name starts with 'S'
i = snames["Customer Name"].value_counts()

# tried this to split names by surname
# surname = df[df["Customer Name"].apply(lambda x: x.split(" "))[1]]



# But this ended up working better:
df['FirstName'] = df['Customer Name'].str.split().str[0]
df["LastName"] = df["Customer Name"].str.split().str[1]

# Searches in Segment column for categories that are either "Consumer" or "Corporate"
f = df.query('Segment == ["Consumer", "Corporate"]')


# Shows counts of most common first and last names:
fname = df["FirstName"].value_counts()
lname = df["LastName"].value_counts()


df["Average Total"] = (df["Sales"] / df["Quantity"]).round(2)

sum_df = df[["Sales","Quantity","Discount"]].sum()


df_sum = pd.DataFrame(data=sum_df).T

df_final = df.append(df_sum, ignore_index=True)



# sns.countplot(data = df, x = df["FirstName"])

# Writes DataFrame above into new excel file, and into New Sheet
"""writer = pd.ExcelWriter("NewSheet.xlsx", engine = "xlsxwriter")

df.to_excel(writer, sheet_name = "superstore_data")

writer.save()"""

end = time.time()

print(end - start)
