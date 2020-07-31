import json

code_input = 'LGA'
airport_code = code_input

with open("airports.json", encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
# print(data)
airports = { b['airport-code'] : b for b in data['airports']}
print("the airports", airports)
location = airports[airport_code]['location']
print("this is your airport Zone", location)