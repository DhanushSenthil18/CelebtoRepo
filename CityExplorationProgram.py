from collections import defaultdict

class City:
    def _init_(self, name, cost, reward):
        self.name = name
        self.cost = cost
        self.reward = reward


connections = defaultdict(list)
city_map = {}
dp = {}


def find_max_reward(current_city, destination, time_left):

    if time_left < 0:
        return float("-inf")

    if current_city == destination:
        return 0

    if (current_city, time_left) in dp:
        return dp[(current_city, time_left)]

    max_reward = float("-inf")

    for next_city, travel_cost in connections[current_city]:

        cost_to_visit = travel_cost + city_map[next_city].cost

        if time_left >= cost_to_visit:
            reward = city_map[next_city].reward + find_max_reward(
                next_city, destination, time_left - cost_to_visit
            )

            max_reward = max(max_reward, reward)

    dp[(current_city, time_left)] = max_reward
    return max_reward


def main():

    cities = [
        City("CITY_A", 300, 1000),
        City("CITY_B", 500, 900),
        City("CITY_C", 250, 1500),
        City("CITY_D", 100, 600),
    ]

    connections_input = [
        ("CITY_A", "CITY_B", 250),
        ("CITY_A", "CITY_D", 300),
        ("CITY_B", "CITY_C", 500),
    ]

    origin = "CITY_A"
    destination = "CITY_C"
    time_available = 7000

    for city in cities:
        city_map[city.name] = city
    # print(city_map)

    for from_city, to_city, travel_cost in connections_input:
        connections[from_city].append((to_city, travel_cost))  # Add connection

    time_after_origin = time_available - city_map[origin].cost

    max_reward = find_max_reward(origin, destination, time_after_origin)

    if max_reward > 0:
        print(f"Maximum Reward: {max_reward + city_map[origin].reward}")
        print(city_map)
    else:
        print("No valid trip plan found within the constraints.")


if _name_ == "_main_":
    main()
