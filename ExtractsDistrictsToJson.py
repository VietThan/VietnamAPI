import csv
import os
import json

# get working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# input & output file names
inputFileName = 'quochoixv.csv'
khoaFileName = 'data.json'
errorFileName = 'error.txt'

khoaOutputFileName = 'khoa.csv'
outputFileName = 'districts.csv'

khoaProvince = {}
khoaDistricts = {}

# extract provinces from khoa's data
with open(os.path.join(__location__, khoaFileName), "r") as khoaFile:
    khoaDict = json.load(khoaFile)
    khoaProvinceKey = 1
    for province, districts in khoaDict.items():
        khoaProvince[khoaProvinceKey] = province
        khoaDistricts[khoaProvinceKey] = districts
        khoaProvinceKey += 1

    print(f'Loaded {khoaProvinceKey-1} rows from Khoa\'s {khoaFileName}')
    khoaFile.close()

# extract list of khoa's districts
khoaDistrictList = {}
count = 1
for khoaProvinceKey, districts in khoaDistricts.items():
    for district, value in districts.items():
        khoaDistrictList[count] = district
        count += 1

print(f'{count-1} districts have been processed from Khoa\'s {khoaFileName}')

inputDistricts = {}

with open(os.path.join(__location__, inputFileName), "r") as inputFile:
    districtReader = csv.DictReader(inputFile)
    unitCount = 1
    districtCount = 1
    for row in districtReader:
        astrDistricts = row["astrDistricts"]
        delimDistricts = astrDistricts.split(',')
        for district in delimDistricts:
            inputDistricts[districtCount] = district
            districtCount+=1
        unitCount +=1

    print(f'{unitCount-1} rows/units have been processed from {inputFileName}')
    print(f'{districtCount-1} districts have been processed from {inputFileName}')

    inputFile.close()


with open(os.path.join(__location__, khoaOutputFileName), "w") as khoaOutput:
    khoaOutput.write('inputDistricKey,strDistricts\n')
    for key,value in khoaDistrictList.items():
        khoaOutput.write(f'{key},{value}\n')
    
with open(os.path.join(__location__, outputFileName), "w") as outputFile:
    outputFile.write('inputDistricKey,strDistricts\n')
    for key,value in inputDistricts.items():
        outputFile.write(f'{key},{value}\n')


