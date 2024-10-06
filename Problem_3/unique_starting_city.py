def find_starting_city(city_distances, gas, mpg):
    n = len(city_distances)
    total_fuel = 0          # Total fuel available for the whole journey
    current_fuel = 0        # Current fuel available 
    start_city = 0          # Evaluates the start city
    
    for i in range(n):
        fuel_gain = gas[i] * mpg      # Converting fuel available to miles
        fuel_needed = city_distances[i] # Calculates distance to next city
        
        total_fuel = total_fuel + (fuel_gain - fuel_needed)    # Calculates whether the fuel is sufficient for entire journey

        current_fuel = current_fuel + (fuel_gain - fuel_needed)  # Calculates whether we can continue from current city to next city

        
        if current_fuel < 0:
            start_city = i + 1   # Marks next city as starting city
            current_fuel = 0     # Resets the fuel for the new starting city
    
    if total_fuel >= 0 :
        return start_city        # Returns the preferred starting city
    else:
        return -1                # Which cannot happen as the questions guarantees one valid starting city


if __name__ == "__main__":
    num_cities = int(input("Enter number of cities: "))
    city_distances = []
    gas = []
    for i in range(num_cities):
        d = int(input(f"Enter distance of city {i}: "))
        city_distances.append(d)
        g = int(input(f"Enter gas amount of city {i}: "))
        gas.append(g)
        
    mpg = int(input("Enter the mpg used for gas: "))
    
    starting_city = find_starting_city(city_distances, gas, mpg)
    print(f"Preferred starting city: {starting_city}")
