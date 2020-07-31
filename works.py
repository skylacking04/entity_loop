given_school_code = input("What is your school code? ")

# save the answer to a variable


print(" you entered school code: ", given_school_code)
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


school_code = given_school_code

for i in data:
    try:
        if (school_code == i['school-code']) or (school_code == i['school-code-2']) or  (school_code == i['school-code-3'])  or  (school_code == i['school-code-4']):
            # print(i['location'])
            new_loc = (i['location'])
            print("Your School Zone is", new_loc)
            break
        else:
            print("ah")
    except:
        pass
print("is this a new  loc? ", new_loc)