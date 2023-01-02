""" The code above is a modified version of the "convert2utf8.py" file that reads in a CSV file specified by the user, converts it to UTF-8 encoding, and saves it to a new CSV file with a name that includes the current date and a counter.

Here are a few notes on the code:

The first input statement asks the user to enter the path to the CSV file.
The second input statement asks the user to enter the desired output filename.
The code removes the quotation marks from the input filename using the replace method.
The codecs.open function is used to open the file with "latin-1" encoding and read it into a Pandas DataFrame.
The datetime module is used to get the current date, and the os module is used to get the number of files in the current directory.
The code then iterates through the files in the current directory and counts the number of files with a name that starts with the output filename specified by the user.
The counter is formatted with leading zeros using the zfill method.
Finally, the code uses the to_csv method of the DataFrame to save the data to a new CSV file with UTF-8 encoding and the current date and counter appended to the name.
This code should allow the user to specify the path to the input CSV file, the desired output filename, and have the current date and a counter appended to the output file name when the file is saved.
 """

import codecs
import pandas as pd
import datetime
import os

# Ask the user to input the path to the CSV file
filename = input("Please enter the path to the CSV file: ")

# Remove the quotation marks from the filename
filename = filename.replace('"', '')

# Ask the user to input the desired output filename
output_filename = input("Please enter the desired output filename: ")

# Open the CSV file with latin-1 encoding
with codecs.open(filename, "r", "latin-1") as f:
    # Read the file into a Pandas DataFrame
    df = pd.read_csv(f)

# Get the current date
now = datetime.datetime.now()
date_str = now.strftime("%Y%m%d")

# Get the number of files with the same name
counter = 0
for file in os.listdir():
    if file.startswith(output_filename):
        counter += 1

# Format the counter with leading zeros
counter_str = str(counter).zfill(3)

# Save the DataFrame to a CSV file with UTF-8 encoding and the current date and counter appended to the name
df.to_csv(f"{output_filename}_{date_str}_{counter_str}.csv", encoding="utf-8", index=False)
