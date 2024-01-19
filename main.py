#!/usr/bin/python3
"""
 Test cities access from a state
"""

from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
st_1 = State(name="California")
print(f"New state: {st_1}")
st_1.save()
st_2 = State(name="Arizona")
print(f"New state: {st_2}")
st_2.save()

city_1_1 = City(state_id=st_1.id, name="Napa")
print(f"New city: {city_1_1} in the state: {st_1}")
city_1_1.save()
city_1_2 = City(state_id=st_1.id, name="Sonoma")
print(f"New city: {city_1_2} in the state: {st_1}")
city_1_2.save()
city_2_1 = City(state_id=st_2.id, name="Page")
print(f"New city: {city_2_1} in the state: {st_2}")
city_2_1.save()


print("\n")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print(f"Find the city {city} in the state {state}")
