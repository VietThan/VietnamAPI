import csv
import os
import json
import urllib.request

# get working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

print(f'working from {__location__}')

# input & output file names
provinceURLpath = "https://vietthan.github.io/VietnamAPI/api/vietnam/provinces.json"
inputFileName = 'quochoixv.csv'
congressDistrictsFileDirectory = 'api/vietnam/congress/districts'

# create output directory
os.makedirs(os.path.join(__location__, congressDistrictsFileDirectory), exist_ok=True)

provinceKeys = {}

with urllib.request.urlopen(provinceURLpath) as provinceURL:
    provinceKeys = json.loads(provinceURL.read().decode())


# Extract Google data
unitDistricts = {}

with open(os.path.join(__location__, inputFileName), "r") as inputFile:
    districtReader = csv.DictReader(inputFile)
    unitCount = 1
    districtCount = 1
    for unit in districtReader:
        # first get province
        intProvinceKey = 0
        strProvinceName = unit["strProvinceName"]
        # verify
        if strProvinceName in provinceKeys:
            # get the districts associated with this unit
            astrDistricts = unit["astrDistricts"]
            delimDistricts = astrDistricts.split(',')
            for district in delimDistricts:
                district = district.strip()
                unitDistricts[districtCount] = {}
                unitDistricts[districtCount]['strDistrictName'] = district
                unitDistricts[districtCount]['strProvinceName'] = strProvinceName
                unitDistricts[districtCount]['intProvinceUnitKey'] = unit['intProvinceUnitKey']
                unitDistricts[districtCount]['intCongressKey'] = unit['intCongressKey']
                unitDistricts[districtCount]['intRepCount'] = unit['intRepCount']

                districtCount+=1
        else:
            print(f'could not find {strProvinceName} in provinces data')




        
        # iterate to the next congressional unit
        unitCount +=1

    print(f'{unitCount-1} rows/units have been processed from {inputFileName}')
    print(f'{districtCount-1} districts have been processed from {inputFileName}')

    inputFile.close()



for intDistrictKey, dictDistrictVal in unitDistricts.items():
    with open(os.path.join(__location__, congressDistrictsFileDirectory, str(intDistrictKey)+'.json'), "w") as unitToDistrictsJson:
        json.dump(dictDistrictVal, unitToDistrictsJson, indent=4, ensure_ascii=False)
        print(f'Finished writing to district unit key {intDistrictKey}')
    unitToDistrictsJson.close()

