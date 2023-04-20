import datetime
import osmnx as ox
import networkx as nx

# Function to calculate ETA
def calculate_eta(distance, speed, rush_hour):
    if rush_hour:
        speed *= 0.5  # Reduce speed by 50% during rush hour
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60
    eta = datetime.datetime.now() + datetime.timedelta(minutes=time_in_minutes)
    return eta.strftime("%Y-%m-%d %H:%M")

# Function to calculate cost
def calculate_cost(distance, cost_per_km):
    return distance * cost_per_km

# Function to get optimal route
def get_optimal_route(origin, destination, mode_of_transport):
    # Retrieve OpenStreetMap data for the area around origin and destination
    G = ox.graph_from_address(origin, network_type='all')
    H = ox.graph_from_address(destination, network_type='all')

    # Merge the graphs for the origin and destination areas
    G = nx.compose(G, H)

    # Check if there are any nodes in the graph
    if not G:
        raise ValueError("No nodes found in graph")

    # Define source and target nodes
    source = next(iter(G.nodes()))
    target = next(iter(G.nodes()))

    # Calculate the shortest path between origin and destination using mode of transport
    if mode_of_transport == 'taxi':
        optimal_route = nx.shortest_path(G, source=source, target=target, weight='travel_time')
    elif mode_of_transport == 'walking':
        optimal_route = nx.shortest_path(G, source=source, target=target, weight='length')
    elif mode_of_transport == 'bus':
        optimal_route = nx.shortest_path(G, source=source, target=target, weight='length')
    elif mode_of_transport == 'train':
        optimal_route = nx.shortest_path(G, source=source, target=target, weight='length')
    else:
        raise ValueError("Invalid mode of transport")

    # Convert optimal route to a list of distance and duration dictionaries
    optimal_route_data = []
    for u, v in zip(optimal_route[:-1], optimal_route[1:]):
        data = G.get_edge_data(u, v)[0]
        distance = data['length']
        duration = distance / (data['maxspeed_kph'] / 60)
        optimal_route_data.append({'distance': {'value': distance}, 'duration': {'value': duration}})

    return optimal_route_data

# Function to handle input errors
def handle_input_error(message):
    while True:
        print(message)
        answer = input("Do you want to continue? (y/n): ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while True:
    # Get user inputs
    origin = input("Enter origin: ")
    while not origin:
        print("Origin cannot be empty")
        origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    while not destination:
        print("Destination cannot be empty")
        destination = input("Enter destination: ")
    distance = input("Enter distance (in km): ")
    while not distance:
        print("Distance cannot be empty")
        distance = input("Enter distance (in km): ")
    try:
        distance = float(distance)
    except ValueError:
        print("Distance must be a number")
        continue
    speed = input("Enter average speed (in km/h): ")
    while not speed:
        print("Speed cannot be empty")
        speed = input("Enter average speed (in km/h): ")
    try:
        speed = float(speed)
    except ValueError:
        print("Speed must be a number")
        continue
    mode_of_transport = input("Enter mode of transport (taxi, bus, train, or walking): ")
    while mode_of_transport not in ['taxi', 'bus', 'train', 'walking']:
        print("Invalid mode of transport. Please choose from taxi, bus, train, or walking.")
        mode_of_transport = input("Enter mode of transport (taxi, bus, train, or walking): ")
    current_time = datetime.datetime.now()

    # Set cost and speed parameters based on mode of transport
    if mode_of_transport == "taxi":
        cost_per_km = 14.3
        rush_hour = True
    elif mode_of_transport == "bus":
        cost_per_km = 6.69655
        rush_hour = False
    elif mode_of_transport == "train":
        cost_per_km = 1.875
        rush_hour = True
    elif mode_of_transport == "walking":
        cost_per_km = 0
        rush_hour = False
        speed = 5  # Set walking speed to 5 km/h

    # Calculate cost and ETA
    cost = calculate_cost(distance, cost_per_km)
    eta = calculate_eta(distance, speed, rush_hour)

    # Get optimal route
    try:
        optimal_route = get_optimal_route(origin, destination, mode_of_transport)
    except Exception as e:
        print(str(e))
        continue

    # Print results
    print(f"Origin: {origin}")
    print(f"Destination: {destination}")
    print(f"Distance: {distance} km")
    print(f"Mode of transport: {mode_of_transport}")
    print(f"Cost: {cost} PHP")
    print(f"ETA: {eta}")
    print(f"Optimal route: {optimal_route}")

    # Ask user if they want to continue
    answer = input("Do you want to calculate another route? (y/n): ")
    if answer.lower() != "y":
        break