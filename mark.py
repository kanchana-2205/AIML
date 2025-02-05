# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 07:12:33 2024

@author: Admin
"""

#read XL
import pandas as pd

df = pd.read_excel("mark.xlsx")
#df = pd.read_csv("mark.csv")
print(df)
print("=============================================")

information=df.info()
print(information)
print("===============================================")

size=df.size
print(size)
print("==================================================")

shape=df.shape
print(shape)
print("=================================================")
c=df.columns
print(c)
print("===================================================")
col = df[["Name","Math"]]
print(col)
col.to_excel("mathmark.xlsx")
#print(df)