given_school_code = input("What is your school code? ")

# save the answer to a variable


print("your sc is ", given_school_code)
data = [
       {
        "location": "New York",
        "school-code": "CITY", 
        "school-code-2": "NYU", 
        "school-code-3": "CityU"
        },
       {
        "location": "New Jersey",
        "school-code": "NJU", 
        "school-code-2": "NJU2", 
        "school-code-3": "NJUE"
       },
       {
        "location": "California",
        "school-code": "CAL",
        "school-code-2": "Cal2"
       },
       {
        "location": "Florida",
        "school-code": "fNJU", 
        "school-code-2": "fNJU2", 
        "school-code-3": "fNJUE"
       }
      
    
    ] 


# for k, v in countries.items():
#     if "1" in v:
#         print k

# given_school_code = 'NJU2'
school_code = given_school_code

for i in data:
    try:
        if (school_code == i['school-code']) or (school_code == i['school-code-2']) or  (school_code == i['school-code-3'])  or  (school_code == i['school-code-4']):
            print(i['location'])
            new_loc = (i['location'])
            print("Your School Zone is", new_loc)
            break
        else:
            print("ah")
    except:
        print("uh oh")



# for i in data:
#     school_code = (i['school-code']) or (i['school-code-2'])
#     if school_code == given_school_code:
#         location = (i['location'])
#         print(i['location'])
#         break



# given_school_code = 'FNJU2'
# for i in data:
#     school_code = (i['school-code'])
#     school_code_2 = (i['school-code-2'])
#     school_code_3 = (i['school-code-3'])
#     # school_code_4 = (i['school-code-4'])
#     # school_code_5 = (i['school-code-5'])
#     # school_code_6 = (i['school-code-6'])
#     # school_code_7 = (i['school-code-7'])
#     # school_code_9 = (i['school-code-8'])
#     print('this is the given school code',given_school_code)
#     if school_code == given_school_code:
#         location = (i['location'])
#         print(i['location'])

#     elif i['school-code-2'] == given_school_code:
#         location = (i['location'])
#         print(i['location'])

#     elif i['school-code-3'] == given_school_code:
#         location = (i['location'])
#         print(i['location'])
#     elif i['school-code-3'] == given_school_code:
#         location = (i['location'])
#         print(i['location'])
#         break
#     else:
#         print('wtf')

        
# # data = [
# #  {
# #    "id_number": "SA4784",
# #    "name": "Mark",
# #    "birthdate": None
# #  },
# #  {
# #    "id_number": "V410Z8",
# #    "name": "Vincent",
# #    "birthdate": "15/02/1989"
# #  },
# #  {
# #    "id_number": "CZ1094",
# #    "name": "Paul",
# #    "birthdate": "27/09/1994"
# #  }
# # ]

# # for i in data:
# #     if i['id_number'] == 'CZ1094':
# #         print(i['birthdate'])
# #         print(i['name'])
# #         break




# # for i in data:
# #     if i['school-code'] or i['school-code-2'] == 'CityU':
# #         print(i['location'])

#         break

# import json

# code_input = 'LGA'
# airport_code = code_input

# with open("airports.json", encoding='utf-8', errors='ignore') as json_data:
#     data = json.load(json_data, strict=False)
# print(data)
# airports = { b['airport-code'] : b for b in data['airports']}
# print("the airports", airports)
# location = airports[airport_code]['location']
# print("this is your airport Zone", location)


# for i in data:
#     if i['school-code'] == 'CityU':
#         print(i['locatoin'])

#         break