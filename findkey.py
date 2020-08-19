# airports = {
#     "JFK": "New York",
#     "LGA": "New York",
#     "EGW": "New Jersey",
#     "FLL": "Florida"
# }


# airports = {
#     "JFK": ["New York", "NY", "Queens"],
#     "LGA": ["New York"],
#     "EGW": ["New Jersey"],
#     "FLL": ["Florida"]
# }
    
#     # for k, v in airport.items():
# for k, v in airports.items():
#     if "Queens" == v or isinstance(v, list) and "Queens" in v:
#         print(k)    




import json


with open("airports2.json", encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
    airport_of_interst = "Florida"
    # for k, v in airport.items():
    for k, v in data.items():
        if airport_of_interst == v or isinstance(v, list) and airport_of_interst in v:
            print(k)