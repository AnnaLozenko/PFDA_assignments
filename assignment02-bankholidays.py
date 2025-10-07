#Northern Ireland bank holdays
#Author: Anna Lozenko

import requests 

#load data from the url (https://www.gov.uk/bank-holidays.json). Data is stored in a json file.
response = requests.get("https://www.gov.uk/bank-holidays.json")
data = response.json()

#PART 1: program that prints out the dates of the bank holidays that happen in northern Ireland.
northern_ireland_holidays = {}

for region in data["northern-ireland"]["events"]:
        northern_ireland_holidays.update({region["title"] : region["date"]})
print(northern_ireland_holidays)


#PART 2: program that prints the bank holidays that are unique to northern Ireland, (i.e. do not happen elsewhere in the UK).
all_uk_holidays = {}
for region in data:
    if region == "northern-ireland":
        continue
    else:
        for holiday in data[region]["events"]:
            all_uk_holidays.update({holiday["title"].lower() : holiday["date"]})
            

unique_ni_holidays = {}
for holiday in data["northern-ireland"]["events"]:
    if holiday["title"].lower() not in all_uk_holidays:
        unique_ni_holidays.update({holiday["title"].lower() : holiday["date"]})
print(unique_ni_holidays)

