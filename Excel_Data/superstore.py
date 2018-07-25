# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import time as time


start = time.time()
df = pd.read_excel("external_files/Superstore.xls")

total = sum(df["Order ID"].apply(lambda x: x.split("-")[0]) == "CA")

total

tot = sum(df["Order ID"].apply(lambda x: x.split("-")[0]) == "US")

snames = df[df["Customer Name"].apply(lambda x: x.startswith("S"))]

pt = pd.pivot_table(df, index = "Customer Name")


pt2 = pd.pivot_table(snames, index = "Customer Name")

# counts data entries of customers who's first name starts with 'S'
i = snames["Customer Name"].value_counts()


# surname = df[df["Customer Name"].apply(lambda x: x.split(" "))[1]]

df['FirstName'] = df['Customer Name'].str.split().str[0]
df["LastName"] = df["Customer Name"].str.split().str[1]



#f = df.query('Segment == ["Consumer", "Corporate"]')



fname = df["FirstName"].value_counts()
lname = df["LastName"].value_counts()


df["Average Total"] = (df["Sales"] / df["Quantity"]).round(2)

sum_df = df[["Sales","Quantity","Discount"]].sum()


df_sum = pd.DataFrame(data=sum_df).T

df_final = df.append(df_sum, ignore_index=True)



# sns.countplot(data = df, x = df["FirstName"])

#writer = pd.ExcelWriter("NewSheet.xlsx", engine = "xlsxwriter")
#
#df.to_excel(writer, sheet_name = "superstore_data")
#
#
#
#writer.save()

end = time.time()

print(end - start)