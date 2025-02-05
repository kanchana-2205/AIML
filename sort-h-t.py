# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 07:16:38 2024

@author: Admin
"""

import pandas as pd
df=pd.read_excel("mark.xlsx")
h=df.head(2)
t=df.tail(2)
print(h)
print(t)
print("\n")
sort=df.sort_values(by=["Math"])
print(sort)
print("\n")
dsort=df.sort_values(by='Math', ascending=False)
print(dsort)
