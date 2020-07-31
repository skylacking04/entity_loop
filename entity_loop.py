airport = {
     "airport-code": "JFK, LGA",
     "homework": [90.0, 97.0, 75.0, 92.0],
     "quizzes": [88.0, 40.0, 94.0],
     "tests": [75.0, 90.0]
 }

alice = {
     "name": "Alice",
     "homework": [100.0, 92.0, 98.0, 100.0],
     "quizzes": [82.0, 83.0, 91.0],
     "tests": [89.0, 97.0]
 }
tyler = {
     "name": "Tyler",
     "homework": [0.0, 87.0, 75.0, 22.0],
     "quizzes": [0.0, 75.0, 78.0],
     "tests": [100.0, 100.0]
 }


New York = {
    "airport-code": "JFK, LGA"

}

New York = {
    "entity_type" : "location"
    "airport": "JFK, LGA"
}


New Jersey = {
    "entity_type" : "location"
    "airport": "EGW"
}

if attribute = any in airport_dict.airport[]:
    return [SlotSet("entity_type",'airport')]
    return [SlotSet("location",location)]

## what about by city? LAX just let the tjhem as the bot, show me la stats. and the bot can do that
## we know that if they say lAX they ware probably flyign into LA but how knows NOT sf
airport = [
    {
    'location': 'New York',
    'airport-code':[ 'JFK', 'LGA', 'EGW']

}, 
{
    'location':'New Jersey',
    'airport-code':['EGW']
},
{
    'location':'California',
    'airport-code':['LAX','SFO']
},
{
    'location':'Florida',
    'airport-code':['MIA', 'FLL']
}
]

for student in students:
    for value in student:
        print (value, "is", student[value])




student = [lloyd, alice, tyler]
for student in students:
    for value in student:
        print (value, "is", student[value])

## works for list
for i in data:
    if i['school-code'] or i['school-code-2'] == 'CityU':
        print(i['location'])

        break


list_of_airport_codes = [ 'JFK', 'LGA', 'EGW', 'LAX', 'FLL', 'MIA', 'SFO']
list_of_hotels = ['Hyatt', 'Hilton', 'Mariott']

list_of_enitity_types = ['airline', 'airport', 'hotel', 'location']



JFK
jfk slot 
airport 


class SetSlotEntityTypeAirport(Action):
    travel_entity_types = [lloyd, alice, tyler]
    for student in students:
    for value in student:
    found_entity = travel_entity_types[value]
    def name(self):
        return "action_set_slot_as_entity_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("entity_type",found_entity)]

set

  "attributes": [
        "airport-code",
        "airport-name",
        "travel-advice",
        "new-services",
        "airport-statement",
        "airport-safety-measures",
        "transit-info",
        "airport-last-verified",
        "airport-info-url",



        {
    "JFK": "New York"
}

## Series of classes to call in the stories.md file
### sets the slots as attributes or entiets. 

class SetSlotEntityTypeAirport(Action):
    def name(self):
        return "action_set_slot_airport_as_entity_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("entity_type","airport")]


class SetSlotEntityTypeHotel(Action):
    def name(self):
        return "action_set_slot_hotel_as_entity_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("entity_type","hotel")]


class SetSlotEntityTypeAirline(Action):
    def name(self):
        return "action_set_slot_airline_as_entity_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("entity_type","airline")]


class SetSlotEntityTypeLocation(Action):
    def name(self):
        return "action_set_slot_location_as_entity_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("entity_type","location")]


## Series of classes to call in the stories.md file
### sets the slots as attributes or entiets. 

class SetSlotAirportStatementAttribute(Action):
    def name(self):
        return "action_set_slot_airport_statement_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airport-statement")]


class SetSlotHotelStatementAttribute(Action):
    def name(self):
        return "action_set_slot_hotel_statement_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","hotel-statement")]


class SetSlotAirlineStatementAttribute(Action):
    def name(self):
        return "action_set_slot_airline_statement_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airline-statement")]


class SetSlotLocationStatementAttribute(Action):
    def name(self):
        return "action_set_slot_location_statement_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","location-statement")]



## Mask Policy
class SetSlotAirportMaskPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_airport_mask_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airport-mask-policy")]



class SetSlotHotelMaskPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_hotel_mask_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","hotel-mask-policy")]


class SetSlotAirlineMaskPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_airline_mask_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airline-mask-policy")]


class SetSlotLocationMaskPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_location_mask_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","location-mask-policy")]


## Clean info
class SetSlotAirportCleanInfoAttribute(Action):
    def name(self):
        return "action_set_slot_airport_clean_info_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airport-clean-info")]


class SetSlotHotelCleanInfoAttribute(Action):
    def name(self):
        return "action_set_slot_hotel_clean_info_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","hotel-clean-info")]


class SetSlotAirlineCleanInfoAttribute(Action):
    def name(self):
        return "action_set_slot_airline_clean_info_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airline-clean-info")]


class SetSlotLocationCleanInfoAttribute(Action):
    def name(self):
        return "action_set_slot_location_clean_info_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","location-clean-info")]



##  cancellatoion policy
class SetSlotAirportCancellationPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_airport_cancellation_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airport-cancellation-policy")]



class SetSlotHotelCancellationPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_hotel_cancellation_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","hotel-cancellation-policy")]


class SetSlotAirlineCancellationPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_airline_cancellation_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","airline-cancellation-policy")]


class SetSlotLocationCancellationPolicyAttribute(Action):
    def name(self):
        return "action_set_slot_location_cancellation_policy_as_attribute"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("attribute","location-cancellation-policy")]




## set slot location
class SetSlotLocationAsNYtAttribute(Action):
    def name(self):
        return "action_set_slot_location_as_new_york"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("location","New York")]
# class SetSlotAirportStatementAttribute(Action):
#     def name(self):
#         return "action_set_slot_airport_statement_as_attribute"

#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("attribute","airport-statement")]





{
    "JFK": "New York",
    "LGA": "New York"
}