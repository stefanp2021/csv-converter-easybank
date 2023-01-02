CSV Converter for Easybank
This repository contains a Python script that converts CSV files from Easybank into a format that can be imported into Firefly.

Prerequisites
Python 3.6 or later
Pandas library for Python
Usage
Clone this repository to your local machine
Navigate to the directory containing the script in your terminal
Run the script using the command python bank.py
Follow the prompts to input the path to the Easybank CSV file and the delimiter used in the file
The converted CSV file will be saved as bank2import.csv in the same directory as the script
Example
Input:

Copy code
Please enter the path to the CSV file: C:\Users\example\Easybank.csv
Please enter the delimiter of the CSV file (e.g. , or ;): ;
Output:

Copy code
Converted CSV file saved as bank2import.csv