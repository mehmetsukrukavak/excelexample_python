import numpy as np
import pandas as pd

dataframe = pd.read_excel("SalarySheet.xlsx")

print(dataframe)

print("#1) Toplamda kaç satır veri vardır?")
print(len(dataframe))
print("#2) Bu firma ortalama ne kadar maaş vermektedir?")
print(dataframe["Salary"].mean())
print("#3) Bu firmada departmanlara göre ortalama maaş karşılaştırması nasıldır?")
print(dataframe.groupby("Department")["Salary"].mean())
print("#4) Bu firmada title (senior - junior) durumuna göre ortalama maaş karşılaştırması nasıldır?")
titleGroup = dataframe.groupby("Title")
print(titleGroup["Salary"].mean())
print("#5) Senior bir kişinin junior bir kişiye göre maaşı ortalama yüzde kaç fazladır?")
print(867.77 / 440.625)
print("#6) Software development departmanında senior bir kişinin junior bir kişiye göre maaşı ortalama ne kadar fazladır?")
group_object_department = dataframe.loc[dataframe["Department"] == "Software Development"].groupby("Title")
print(group_object_department["Salary"].mean())
print(1030.00 / 790.00)
print("#8) Software development departmanında c-level çalışan sayısı marketing departmanında çalışana oranla kaç kat fazladır?")
print(dataframe.loc[dataframe["Department"] == "Software Development"].groupby("Title").describe())
print(dataframe.loc[dataframe["Department"] == "Marketing"].groupby("Title").describe())
print(6/2)