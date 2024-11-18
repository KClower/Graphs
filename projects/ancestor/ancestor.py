
def earliest_ancestor(ancestors, starting_node):
    """
    Find the earliest known ancester fo the given starting node.

    Args:
        ancestors: List of tuples representing (parent, child) relationships.
        starting_node: The node for which to find the earliest ancestor.

    Returns:
        The earliest ancestor's ID or -1 if no ancestor exists.
    """
    # Build the graph: child -> set of parents
    graph = {}
    for parent, child in ancestors:
        if child not in graph:
            graph[child] = set()
        graph[child].add(parent)

    # If the starting node has no parents, return -1
    if starting_node not in graph:
        return -1
    
    # DFS (depth-first-search) to find the earliest ancestor
    stack = [(starting_node, 0)] # Stack holds (currentnode, depth)
    max_depth = -1
    earliest_ancestor_id = -1

    while stack:
        current_node, depth = stack.pop()

        # If we find a deeper ancestor or one with a smaller ID at the same depth
        if (depth > max_depth) or (depth == max_depth and current_node < earliest_ancestor_id):
            max_depth = depth
            earliest_ancestor_id = current_node

        # Add parents to the stack with incremented depth
        for parent in graph.get(current_node, []):
            stack.append((parent, depth + 1))
    
    return earliest_ancestor_id