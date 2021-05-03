'''
Extract provinces.csv to json

Assume csv is sorted by intProvinceKey
Assume csv headers:
intProvinceKey and strProvinceName
'''
import csv
import os
import json

# get working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# input & output file names
inputFileName = 'provinces.csv'
outputFileName = 'api/vietnam/provinces.json'
outputFileDirectory = 'api/vietnam/'

# create output directory
os.makedirs(os.path.join(__location__, outputFileDirectory), exist_ok=True)

# set up dict to be used in json writing
provincesDict = {}

# read input csv
with open(os.path.join(__location__, inputFileName), "r") as provincesFile:
    provincesReader = csv.DictReader(provincesFile)
    lineCount = 0
    for row in provincesReader:
        # read and store in dict the correct way
        intProvinceKey = int(row["intProvinceKey"])
        strProvinceName = row["strProvinceName"]
        provincesDict[strProvinceName] = intProvinceKey
        lineCount += 1
    print(f"Processed {lineCount} lines from {inputFileName}")

# write to provinces.json
with open(os.path.join(__location__, outputFileName), "w") as provincesJson:
    json.dump(provincesDict, provincesJson, indent=4, ensure_ascii=False)
    print(f'Finished writing to {outputFileName}')