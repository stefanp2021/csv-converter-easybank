from pickle import FALSE
import pandas as pd
import copy
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'import\EASYBANK_Umsatzliste_20220106_2150.csv')

print(dirname)

df_bank = pd.read_csv(filename, index_col=False, sep=";",header=None)
df_shape = df_bank.shape
df_shape_column = df_shape[1]
list_columnname = []
for i in range(df_shape_column):
    a = "column_{i}".format(i=i)
    list_columnname.append(a)



df_bank_split = copy.copy(df_bank)
df_bank_split.columns = list_columnname

#https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators


df_bank_split[["Number_before","Number_within"]] = df_bank_split["column_1"].str.split("(?= AT)", 0, expand=True)
df_bank_split["Number_within"] = df_bank_split["Number_within"].str.lstrip()


#print(df_bank_split.head())


df_bank_split[["First","Second"]] = df_bank_split["Number_before"].str.split("(?= DE)", 1, expand=True)
df_bank_split = df_bank_split.drop(["Number_before"], axis=1,errors="ignore")
df_bank_split["Second"] = df_bank_split["Second"].str.lstrip()

#print(df_bank_split.head())


#list_sort_name = ["column_0","column_1","First","Second","Number_within","column_3","column_4","column_5"]


#df_bank_split = df_bank_split.reindex(columns=list_sort_name)

#print(df_bank_split.head())

#df_bank_split.to_csv("test.csv",index=False,header=True, sep=";")


df = copy.copy(df_bank_split)
df[["AT_before","AT_after"]] = df["Number_within"].str.split(" ", 1, expand=True)
df = df.drop(["Number_before"], axis=1,errors="ignore")
print(df.shape)
list_sort_name_1 = ["column_0","column_1","First","Second","AT_before","AT_after","column_3","column_4","column_5","column_6","column_7"]
df = df.reindex(columns=list_sort_name_1)
df.to_csv("bank2import.csv",index=False,header=True, sep=";")