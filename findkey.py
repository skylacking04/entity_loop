airports = {
    "JFK": "New York",
    "LGA": "New York",
    "EGW": "New Jersey",
    "FLL": "Florida"
}
    


for k, v in airports.items():
    if "New York" == v or isinstance(v, list) and "1" in v:
        print(k)