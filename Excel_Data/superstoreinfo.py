# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
from pandas import ExcelWriter



df = pd.read_excel("external_files/SuperStore.xls")

df.head()

# Listing and counting all the cities
val = df["City"].value_counts()


info = df["City"] # listing all the cities


# Graphs data by Ship mode, and counts total based on type
# g = sns.countplot(data=df, x = df["Ship Mode"])


# cal contains all sales from California with 7 or greater quantity 
cal = df[(df["Quantity"] >= 7) & (df["State"] == "California")]

# Sort by city on x, and state by Y, and then count based on Region
e = df.groupby(by=["State", "Quantity"]).count()["Sales"].unstack()

sns.boxplot(x="Quantity", y="Profit", palette=["m", "g"],
            data=cal)
sns.despine(offset=10, trim=True)

pt = pd.pivot_table(df, index = "Sub-Category")

