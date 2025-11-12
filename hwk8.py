# Name:  - Nargiz, Marybella, Tana, Tulip 
# Peers:  - N/A 
# References:  - N/A 

def make_graph() -> dict[str, dict[str,int]]:
    """Make the graph repersentning campus locations and weights between them
    :returns: dict graph of nodes and weights
    """
    graph:dict[str, dict[str,int]] = {}
    graph["athletic fields"] = {}
    graph["athletic fields"]["lamont bridge"] = 10
    graph["lamont bridge"] = {}
    graph["lamont bridge"]["athletic fields"] = 10
    graph["burton lawn"] = {}
    graph["burton lawn"]["seelye lawn"] = 3 
    graph["burton lawn"]["lanning fountain"] = 4 
    graph["burton lawn"]["rock park"] = 5 
    graph["capen garden"] = {}
    graph["capen garden"]["conway gazebo"] = 1
    graph["capen garden"]["davis lawn"] = 1
    graph["chapin lawn"] = {}
    graph["chapin lawn"]["seelye lawn"] = 2
    graph["chapin lawn"]["cutter courtyard"] = 8
    graph["chapin lawn"]["rock garden"] = 4
    graph["conway gazebo"] = {}
    graph["conway gazebo"]["capen garden"] = 1
    graph["grecourt gates"] = {}
    graph["grecourt gates"]["seelye lawn"] = 6
    graph["grecourt gates"]["trudys garden"] = 9
    graph["happy chace garden"] = {}
    graph["happy chace garden"]["japanese garden"] = 4
    graph["happy chace garden"]["systematics garden and perennial border"] = 5
    graph["happy chace garden"]["quad lawn"] = 3
    graph["japanese garden"] = {}
    graph["japanese garden"]["happy chace garden"] = 4
    graph["lamont bridge"]["rock park"] = 7
    graph["lanning fountain"] = {}
    graph["lanning fountain"]["rock garden"] = 4
    graph["lanning fountain"]["systematics garden and perennial border"]  = 2
    graph["lanning fountain"]["rock park"] = 9
    graph["lanning fountain"]["burton lawn"] = 3
    graph["seelye lawn"] = {}
    graph["seelye lawn"]["chapin lawn"] = 2
    graph["seelye lawn"]["grecourt gates"] = 6
    graph["seelye lawn"]["burton lawn"] = 3
    graph["rock garden"] = {}
    graph["rock garden"]["chapin lawn"] = 4
    graph["rock garden"]["systematics garden and perennial border"] =1
    graph["rock garden"]["lanning fountain"] = 4
    graph["rock park"] = {}
    graph["rock park"]["lanning fountain"] = 9
    graph["rock park"]["lamont bridge"] = 7
    graph["rock park"]["burton lawn"] = 5
    graph["rock park"]["systematics garden and perennial border"] = 10
    graph["systematics garden and perennial border"] = {}
    graph["systematics garden and perennial border"]["happy chace garden"] = 5
    graph["systematics garden and perennial border"]["rock garden"] = 1
    graph["systematics garden and perennial border"]["lanning fountain"] = 2
    graph["systematics garden and perennial border"]["rock park"] = 10
    graph["trudys garden"] = {}
    graph["trudys garden"]["grecourt gates"] = 9
    graph["davis lawn"] = {}
    graph["davis lawn"]["cutter courtyard"] = 2
    graph["davis lawn"]["capen garden"] = 1
    graph["cutter courtyard"] = {}
    graph["cutter courtyard"]["davis lawn"] = 2
    graph["cutter courtyard"]["chapin lawn"] = 8
    graph["quad lawn"] = {}
    graph["quad lawn"]["happy chace garden"] = 3
    return graph


def get_initial_parents(graph:dict[str, dict[str,int]], initial:str) -> dict[str,str|None]:
    """Gets the inital parents for each node in the graph
    :param graph:(dict[str, dict[str,int]]): Initial graph of nodes and weights
    :param initial: (str) the starting node
    :retuns: dict[str,str|None] graph of nodes and their parents
    """
    parents:dict[str,str|None] = {}
    for node in graph.keys():
        if  node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents
    
def get_initial_costs(graph:dict[str, dict[str,int]], initial:str) -> dict[str, float]:
    """Gets the intial costs for each edge in the graph
    :param graph: (dict[str, dict[str,int]]) Initial graph of nodes and weights
    :param initial: (str): The starting node
    :retuns: dict[str, float] the graph of nodes and their costs
    """
    costs:dict[str,float] = {}
    for node in graph.keys():
        if node != initial:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs

def find_lowest_cost_node(costs:dict[str,float], processed:list[str]) -> str|None:
    """Finds the lowest cost node in the graph that has not been processed yet
    :param costs: (dict[str,float]) graph nodes and their costs
    :param processed: (list[str]): list of processed nodes
    :returns:str|None: the lowest cost node that hasn't been processed yet
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost #new lowest cost node
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra(graph:dict[str, dict[str,int]], start:str, finish:str) -> list[str] : #look at output type
    """Run Dijkstra's algorithm to find the shortest path between start and finish nodes
    :param graph: (dict[str, dict[str,int]]) The initial graph of nodes and weights
    :param start: (str) The starting node
    :param finish: (str) The ending node
    :retuns: list[str] The shortest path from start node to end node
    """
    processed:list[str] = []
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
        parent = parents[node]
        if parent != None:
            node = parent
            path = [node] + path
    return path

#Main:
def main():
    graph = make_graph()
    #print("Graph:", graph)
    start = "athletic fields"
    finish = "lamont bridge"
    path = run_dijkstra(graph,start,finish)
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"capen garden","burton lawn")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"burton lawn","seelye lawn")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"quad lawn","japanese garden")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"seelye lawn","lanning fountain")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"cutter courtyard","grecourt gates")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"conway gazebo","davis lawn")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"lanning fountain","rock park")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"rock park","conway gazebo")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"chapin lawn","quad lawn")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"chapin lawn","systematics garden and perennial border")
    print("The shortest path is", path)
    
    path = run_dijkstra(graph,"athletic fields","conway gazebo")
    print("The shortest path is", path)
    
    print("Possible Locations: athletic fields, burton lawn, capen garden,chapin lawn, conway gazebo, grecourt gates, happy chace garden,japanese garden,lamont bridge,lanning fountain,seelye lawn,rock garden,rock park,systematics garden and perennial border,trudys garden, davis lawn, cutter courtyard, quad lawn")
    input_start = input("Enter Starting Location: ").strip().lower()
    while input_start not in graph.keys():
        print("Invalid starting location. Please try again.")
        input_start = input("Enter Starting Location: ").strip().lower()
    input_finish = input("Enter Ending Location: ").strip().lower()
    while input_finish not in graph.keys():
        print("Invalid ending location. Please try again.")
        input_finish = input("Enter Ending Location: ").strip().lower()
    path = run_dijkstra(graph,input_start,input_finish)
    print("The shortest path is", path)

if __name__ == "__main__":
    main()
