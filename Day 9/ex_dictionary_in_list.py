travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name: str, times_visited: int, cities_visited: list) -> None:
    travel_log.append(
        {
            "country": country_name,
            "visits": times_visited,
            "cities": cities_visited
        }
    )
    print(f"You've visited {country_name} {times_visited} times.")
    print(f"You've been to {' and '.join(city for city in cities_visited)}")



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
