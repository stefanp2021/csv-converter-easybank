from pickle import FALSE
import pandas as pd
import copy
import os

# Ask the user to input the path to the CSV file and the delimiter of the file
filename = input("Please enter the path to the CSV file: ")
delimiter = input("Please enter the delimiter of the CSV file (e.g. , or ;): ")

# Read in the CSV file and store it in a Pandas DataFrame
df_bank = pd.read_csv(filename, index_col=False, sep=delimiter, header=None)

print("now processing "+filename)

df_bank = pd.read_csv(filename, index_col=False, sep=delimiter,header=None)
df_shape = df_bank.shape
df_shape_column = df_shape[1]
list_columnname = []
for i in range(df_shape_column):
    a = "column_{i}".format(i=i)
    list_columnname.append(a)

df_bank_split = copy.copy(df_bank)
df_bank_split.columns = list_columnname

df_bank_split[["Number_before","Number_within"]] = df_bank_split["column_1"].str.split("(?= AT)", 0, expand=True)
df_bank_split["Number_within"] = df_bank_split["Number_within"].str.lstrip()

df_bank_split[["First","Second"]] = df_bank_split["Number_before"].str.split("(?= DE)", 1, expand=True)
df_bank_split = df_bank_split.drop(["Number_before"], axis=1,errors="ignore")
df_bank_split["Second"] = df_bank_split["Second"].str.lstrip()

df = copy.copy(df_bank_split)
df[["AT_before","AT_after"]] = df["Number_within"].str.split(" ", 1, expand=True)
df = df.drop(["Number_before"], axis=1,errors="ignore")
print(df.shape)
list_sort_name_1 = ["column_0","column_1","First","Second","AT_before","AT_after","column_3","column_4","column_5","column_6","column_7"]
df = df.reindex(columns=list_sort_name_1)

# Ask the user for the desired output filename
output_filename = input("Please enter the desired output filename: ")

df.to_csv(output_filename,index=False,header=True, sep=";")
