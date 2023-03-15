
# airplane travel example for Dijkstra's Algorithm
# city class
from typing import List,Dict

class City:
    def __init__(self, name:str):
        self.name = name
        self.adjacent_city = {}
    
    def __repr__(self):
        return self.name

    def add_adjacent(self, city, cost):
        self.adjacent_city[city] = cost
    

def cheapest_unvisited_cities(unvisited_cities: List[City], cheapest_price_table:Dict):
    return sorted(unvisited_cities, key=lambda x : cheapest_price_table.get(x))

# function for finding cheapest path from starting city to destination city
def dijkstra(starting_city: City, destination_city: City):
    
    cheapest_price_table={}
    cheapest_previous_stopover_table={}
    visited_cities={}

    unvisited_cities = []
    cheapest_price_table[starting_city] = 0
    unvisited_cities.append(starting_city)

    current_city = starting_city 
    while current_city:
        visited_cities[current_city] = True
        unvisited_cities.remove(current_city)

        # loop through all adjacent city
        for city,price in current_city.adjacent_city.items():
            # check if unvisited
            if visited_cities.get(city) is None:
                unvisited_cities.append(city)

            # calculate price of getting from starting city to adjacent city using current city as second to last stop
            price_through_current_city = cheapest_price_table.get(current_city) + price

            # check if cheapest
            if cheapest_price_table.get(city) is None or (price_through_current_city < cheapest_price_table.get(city)):
                cheapest_price_table[city] = price_through_current_city
                cheapest_previous_stopover_table[city] = current_city.name

        if len(unvisited_cities) != 0:
            current_city = cheapest_unvisited_cities(unvisited_cities, cheapest_price_table)[0]
        else:
            return cheapest_previous_stopover_table


if __name__ == "__main__":
    atlanta = City("Atlanta")
    boston = City("Boston")
    chicago = City("Chicago")
    denver = City("Denver")
    el_paso = City("El Paso")

    atlanta.add_adjacent(boston, 100)
    atlanta.add_adjacent(denver, 160)
    boston.add_adjacent(chicago, 120)
    boston.add_adjacent(denver, 180)
    chicago.add_adjacent(el_paso, 80)
    denver.add_adjacent(chicago, 40)
    denver.add_adjacent(el_paso, 140)

    cheapest = dijkstra(atlanta, el_paso)
