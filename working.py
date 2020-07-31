given_airport_code = input("What is your airport code? ")

# save the answer to a variable


print("your airport code is ", given_airport_code)
data = [
       {
        "location": "New York",
        "airport-code": "JFK", 
        "airport-code-2": "LGA", 
        "airport-code-3": "LON"
        },
       {
        "location": "New Jersey",
        "airport-code": "EGW"
       },
       {
        "location": "California",
        "airport-code": "SFO",
        "airport-code-2": "LAX"
       },
       {
        "location": "Florida",
        "airport-code": "FLL", 
        "airport-code-2": "OCM", 
        "airport-code-3": "MIA"
       }
      
    
    ] 

airport_code = given_airport_code

for i in data:
    try:
        if (airport_code == i['airport-code']) or (airport_code == i['airport-code-2']) or  (airport_code == i['airport-code-3'])  or  (airport_code == i['airport-code-4']):
            print(i['location'])
            new_loc = (i['location'])
            print("Your Location is ", new_loc)
            break
        else:
            print("ah")
    except:
        pass



