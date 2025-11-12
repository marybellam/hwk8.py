# Name:  - Nargiz, Marybella, Tana, Tulip 
# Peers:  - N/A 
# References:  - N/A 

def make_graph() -> dict:
    graph = {}
    graph["athletic_Fields"] = {}
    graph["athletic_Fields"]["lamont_Bridge"] = 10
    graph["lamont_Bridge"] = {}
    graph["lamont_Bridge"]["athletic_Fields"] = 10
    graph["burton_Lawn"] = {}
    graph["burton_Lawn"]["seelye_Lawn"] = 3 
    graph["burton_Lawn"]["lanning_Fountain"] = 4 
    graph["burton_Lawn"]["rock_Park"] = 5 
    graph["capen_Garden"] = {}
    graph["capen_Garden"]["conway_Gazebo"] = 1
    graph["capen_Garden"]["davis_Lawn"] = 1
    graph["chapin_Lawn"] = {}
    graph["chapin_Lawn"]["seelye_Lawn"] = 2
    graph["chapin_Lawn"]["cutter_Courtyard"] = 8
    graph["chapin_Lawn"]["rock_Garden"] = 4
    graph["conway_Gazebo"] = {}
    graph["conway_Gazebo"]["capen_Garden"] = 1
    graph["grecourt_Gate"] = {}
    graph["grecourt_Gate"]["seelye_Lawn"] = 6
    graph["grecourt_Gate"]["trudys_Garden"] = 9
    graph["happy_Chace_28_Garden"] = {}
    graph["happy_Chace_28_Garden"]["japanese_Garden"] = 4
    graph["happy_Chace_28_Garden"]["systematics_Garden_and_Perennial_Border"] = 5
    graph["happy_Chace_28_Garden"]["quad_Lawn"] = 3
    graph["japanese_Garden"] = {}
    graph["japanese_Garden"]["happy_Chace_28_Garden"] = 4
    graph["lamont_Bridge"]["rock_Park"] = 7
    graph["lanning_Fountain"] = {}
    graph["lanning_Fountain"]["rock_Garden"] = 4
    graph["lanning_Fountain"]["systematics_Garden_and_Perennial_Border"]  = 2
    graph["lanning_Fountain"]["rock_Park"] = 9
    graph["lanning_Fountain"]["burton_Lawn"] = 3
    graph["seelye_Lawn"] = {}
    graph["seelye_Lawn"]["chapin_Lawn"] = 2
    graph["seelye_Lawn"]["grecourt_Gate"] = 6
    graph["seelye_Lawn"]["burton_Lawn"] = 3
    graph["rock_Garden"] = {}
    graph["rock_Garden"]["chapin_Lawn"] = 4
    graph["rock_Garden"]["systematics_Garden_and_Perennial_Border"] =1
    graph["rock_Garden"]["lanning_Fountain"] = 4
    graph["rock_Park"] = {}
    graph["rock_Park"]["lanning_Fountain"] = 9
    graph["rock_Park"]["lamont_Bridge"] = 7
    graph["rock_Park"]["burton_Lawn"] = 5
    graph["rock_Park"]["systematics_Garden_and_Perennial_Border"] = 10
    graph["systematics_Garden_and_Perennial_Border"] = {}
    graph["systematics_Garden_and_Perennial_Border"]["happy_Chace_28_Garden"] = 5
    graph["systematics_Garden_and_Perennial_Border"]["rock_Garden"] = 1
    graph["systematics_Garden_and_Perennial_Border"]["lanning_Fountain"] = 2
    graph["systematics_Garden_and_Perennial_Border"]["rock_Park"] = 10
    graph["trudys_Garden"] = {}
    graph["trudys_Garden"]["grecourt_Gate"] = 9
    graph["davis_Lawn"] = {}
    graph["davis_Lawn"]["cutter_Courtyard"] = 2
    graph["davis_Lawn"]["capen_Garden"] = 1
    graph["cutter_Courtyard"] = {}
    graph["cutter_Courtyard"]["davis_Lawn"] = 2
    graph["cutter_Courtyard"]["chapin_Lawn"] = 8
    graph["quad_Lawn"] = {}
    graph["quad_Lawn"]["happy_Chace_28_Garden"] = 3
    return graph


def get_initial_parents(graph:dict[str, dict[str,int]], initial:str) -> dict:
    parents = {}
    for node in graph.keys():
        if node is not None and node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents
    
def get_initial_costs(graph:dict[str, dict[str,int]], initial:str) -> dict[str, int]:
    costs = {}
    for node in graph.keys():
        if node != None and node != initial:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs

def find_lowest_cost_node(costs:dict, processed:list) -> str:
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra(graph:dict[str, dict[str,int]], start:str, finish:str) -> list[str]:
    processed = [] 
    parents = get_initial_parents(graph, start)
    costs = get_initial_costs(graph, start)
    node = find_lowest_cost_node(costs,processed)

    while node is not None:     
        cost = costs[node]
        neighbors = graph[node] 
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs.get(n, float("inf")) > new_cost: #if costs[n] > new_cost:
                costs[n] = new_cost 
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)

    path = [finish] 
    node = finish
    while (node != start):
        if parents[node] != None:
            node = parents[node]
            path = [node] + path
    return path


#Main:
def main():
    graph = make_graph()
    #print("Graph:", graph)
    start = "athletic_Fields"
    finish = "lamont_Bridge"
    path = run_dijkstra(graph,start,finish)
    print("The shortest path is", path)
    
    start = "capen_Garden"
    finish = "burton_Lawn"
    path = run_dijkstra(graph,start,finish)
    print("The shortest path is", path)

if __name__ == "__main__":
    main()
