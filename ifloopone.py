data = [
       {
        "location": "New York",
        "school-code": "CITY", 
        "school-code-2": "CityU", 
        "school-code-3": "AKO2"
        },
       {
        "location": "New Jersey",
        "school-code": "NJU", 
        "school-code-2": "NJU2", 
        "school-code-3": "NJUE"
       },
       {
        "location": "California",
        "school-code": "CAL"
       },
       {
        "location": "Florida",
        "school-code":"OAK",   
        "school-code-2": "CityU2", 
        "school-code-3": "AKgO"  
        }
        ]

for i in data:
    if i['school-code'] == 'AKO':
        location = (i['location'])
        print(i['location'])
        break
    elif i['school-code-3'] == 'AKO':
        location = (i['location'])
        print(i['location'])
        break

        
# data = [
#  {
#    "id_number": "SA4784",
#    "name": "Mark",
#    "birthdate": None
#  },
#  {
#    "id_number": "V410Z8",
#    "name": "Vincent",
#    "birthdate": "15/02/1989"
#  },
#  {
#    "id_number": "CZ1094",
#    "name": "Paul",
#    "birthdate": "27/09/1994"
#  }
# ]

# for i in data:
#     if i['id_number'] == 'CZ1094':
#         print(i['birthdate'])
#         print(i['name'])
#         break




# for i in data:
#     if i['school-code'] or i['school-code-2'] == 'CityU':
#         print(i['location'])

#         break

# import json

# code_input = 'LGA'
# airport_code = code_input

# with open("airports.json", encoding='utf-8', errors='ignore') as json_data:
#     data = json.load(json_data, strict=False)
# # print(data)
# # airports = { b['airport-code'] : b for b in data['airports']}
# # print("the airports", airports)
# # location = airports[airport_code]['location']
# # print("this is your airport Zone", location)


# for i in data:
#     if i['school-code'] == 'CityU':
#         print(i['locatoin'])

#         break