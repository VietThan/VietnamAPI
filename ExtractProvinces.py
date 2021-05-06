import csv
import os
import json
import urllib.request

# get working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# input & output file names
provinceURLpath = 'https://vietthan.github.io/VietnamAPI/api/vietnam/provinces.json'
inputFileName = 'quochoixv.csv'
provinceFileDirectory = 'api/vietnam/provinces/'
provDisFileDirectory = 'api/vietnam/provinces/districts/'
outputFileName = 'ProvincesToDistricts.json'

# create output directory
os.makedirs(os.path.join(__location__, provinceFileDirectory), exist_ok=True)
os.makedirs(os.path.join(__location__, provDisFileDirectory), exist_ok=True)

provinceKeys = {}

with urllib.request.urlopen(provinceURLpath) as provinceURL:
    provinceKeys = json.loads(provinceURL.read().decode())

# Extract Google data
inputDistricts = {}
provinceDistricts = {}

with open(os.path.join(__location__, inputFileName), "r") as inputFile:
    districtReader = csv.DictReader(inputFile)
    unitCount = 1
    districtCount = 1
    for unit in districtReader:
        # get districts and put in the right province

        # first get province
        intProvinceKey = 0
        strProvinceName = unit["strProvinceName"]
        # verify
        if strProvinceName in provinceKeys:
            # setup province if hasn't already
            if strProvinceName not in provinceDistricts:
                    provinceDistricts[strProvinceName] = {}

            intProvinceKey = provinceKeys[strProvinceName]
            '''
            # make sure province key is in
            if intProvinceKey not in provinceDistricts[strProvinceName]:
                provinceDistricts[strProvinceName]['intProvinceKey'] = intProvinceKey
            '''
            
            # get the districts associated with this unit
            astrDistricts = unit["astrDistricts"]
            delimDistricts = astrDistricts.split(',')
            for district in delimDistricts:
                district = district.strip()
                inputDistricts[districtCount] = district
                provinceDistricts[strProvinceName][district] = districtCount
                # increment to the next district
                districtCount+=1


        else:
            print(f'could not find {strProvinceName} in provinces data')




        
        # iterate to the next congressional unit
        unitCount +=1

    print(f'{unitCount-1} rows/units have been processed from {inputFileName}')
    print(f'{districtCount-1} districts have been processed from {inputFileName}')

    inputFile.close()

# write to provinces.json
with open(os.path.join(__location__, provinceFileDirectory, outputFileName), "w") as provincesToDistrictsJson:
    json.dump(provinceDistricts, provincesToDistrictsJson, indent=4, ensure_ascii=False)
    print(f'Finished writing to {outputFileName}')

provincesToDistrictsJson.close()