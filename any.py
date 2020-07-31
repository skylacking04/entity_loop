import json



code_input = 'CITYU'
school_code = code_input
print('scool code is', school_code)
with open("schools.json", encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
# print(data)
schools = { b['school-code-2'] : b for b in data['schools']}
# print(schools)
location = schools[school_code]['location']
print("Your school zone is ", location)

# code_input = 'CityU'
# school_code = code_input

# with open("schools.json", encoding='utf-8', errors='ignore') as json_data:
#     data = json.load(json_data, strict=False)
# # print(data)
# # for i in range(1,10):
# #     num = range(6) 
# try:
#     schools = { b['school-code'] : b for b in data['schools']}
# except:
#     print("darn")
# else:
#     schools = { b['school-code-2'] : b for b in data['schools']}
# print(schools)
# location = schools[school_code]['location']
# print("this is your school Zone", location)

















# name = 'Blue Air'
# with open("airlines.json", encoding='utf-8', errors='ignore') as json_data:
#     data = json.load(json_data, strict=False)
# print(data)
# airlines = { b['name'] : b for b in data['airlines']}
# print(airlines)
# icao = airlines[name]['icao']
# print("this is icao", icao)
    
    # text = ( "This is your airline: {name} and this is the icao code: {icao}"
    # ).format(
    #     name=name,
    #     icao=icao
        
        
#  def start(self):
#             name = self.db.flow.get('airlinename') or \
#                 self.properties.get('airlinename') or "American Airlines"
#         url = API_URL
#         data = requests.get(url).json()
#         airlines = { b['name'] : b for b in data['airlines']}
#         icao = airlines[name]['icao']
       
#         text = ( "This is your airline: {name} and this is the icao code: {icao}"
#         ).format(
#            name=name,
#            icao=icao
           
        









     
# data = {
#      "schools" : [
#          {
#              'location':'New York','school-code':[ 'MGOA', 'CityU', 'AKO'], 
#              'location':'New Jersey','school-code':['GOE'],
#              'location':'California','school-code':['OAS','STO'],
#              'location':'Florida','school-code':['CDY','OAK']

                            
    
# }
#      ]
#  }

# data_file_path = "schools.json"
# with open(data_file_path, 'r') as j:
#      contents = json.loads(j.read())
#      print(j)




# data = requests.get('/home/ram/entity_loop/schools.json').json()
# school = { b['name'] : b for b in data['schools']}
# print(data['schools'])


# schools= { b['school-code'] : b for b in data['airlines']}
# icao = airlines[school-code]['icao']

    # def start(self):
    #     name = self.db.flow.get('airlinename') or \
    #         self.properties.get('airlinename') or "American Airlines"
    #     url = API_URL
    #     # data = requests.get(url).json()
    #     airlines = { b['name'] : b for b in data['airlines']}
    #     icao = airlines[name]['icao']
       
    #     text = ( "This is your airline: {name} and this is the icao code: {icao}"
    #     ).format(
    #        name=name,
    #        icao=icao
           
        
    #     )
    #     message = self.create_message(text=text)
    #     return self.respond(message=message, action="next")
        


# countries = {
#         "Normal UK project" : "1",
#         "UK Omnibus project" : "1-Omni",
#         "Nordic project" : ["11","12","13","14"],
#         "German project" : "21",
#         "French project" : "31"
#         }
# b = '11'
# for k, v in countries.items():
#     if b == v or isinstance(v, list) and "11" in v:
#         print(k)





# schools = {
          
#     'location':'New York','school-code':[ 'MGOA', 'CityU', 'AKO'], 
#     'location':'New Jersey','school-code':['GOE'],
#     'location':'California','school-code':['OAS','STO'],
#     'location':'Florida','school-code':['CDY','OAK']
# }
# print(schools[0])

# # b = "CityU"




# l = [i['location'] for i in schools if code_input in i['school-code']][0]
# print("Your school zone is",l)


# code_input = 'CityU'
# l = [i['location'] for i in schools if code_input in i['school-code']][0]
# print("Your school zone is",l)

# x = next((d['location'] for d in schools if code_input in d["school-code"]), None)
# print(x)
# # a




# best to simply state the issue. Thanks for the links – skylacking 29 secs ago    Edit   
# add a comment
# 2 Answers
# Active
# Oldest
# Votes

# 2


# This can be done using next and a simple generator comprehension:

# next(d['location'] for d in schools if code_input in d['school-code'])
# This will raise an error if there are no matches. If this is not desired then you can provide a default return value:

# next((d['location'] for d in schools if code_input in d['school-code']), None)
# share  edit  follow  flag 
# edited 1 hour ago
# answered 1 hour ago

# Jab
# 19k1919 gold badges6464 silver badges107107 bronze badges
# 1

# interesting.. didnt know next() can be used like that.. thank you – Boyke Ferdinandes 1 hour ago
# add a comment

# 0


# Try this -

# code_input = 'CityU'
# l = [i['location'] for i in schools if code_input in i['school-code']][0]
# print("Your school zone is",l)
# Your school zone is New York
# share  edit  follow  flag 
# ans