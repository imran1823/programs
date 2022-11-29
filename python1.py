def a_star(graph, start, goal):
    """Finds the shortest path from start to goal in a graph using A*."""
 
    # The set of nodes already evaluated.
closed_set = set()
 
    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
open_set = set([start])
 
    # The map of navigated nodes.
came_from = {}
 
    # The cost of getting from the start node to each node.
g_score = {start: 0}
 
    # The total cost of getting from the start to the goal
    # by passing by that node. That value is partly known, partly heuristic.
f_score = {start: graph.heuristic_cost_estimate(start, goal)}
 
while open_set:
        # Get the node in the open set with the lowest f_score.
current = min((f_score[node], node) for node in open_set)[1]
 
if current == goal:
    return