# Binary Search implementation
def binary_search(arr, target):
    """
    Perform binary search on a sorted array
    
    Args:
        arr: A sorted list of elements
        target: The element to search for
    
    Returns:
        Index of the target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Element is not present in array
    return -1

# Quick Sort implementation
def quick_sort(arr):
    """
    Sort an array using the quick sort algorithm
    
    Args:
        arr: A list of elements to sort
    
    Returns:
        A sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Breadth-First Search implementation
def bfs(graph, start_node):
    """
    Perform BFS traversal starting from a given node
    
    Args:
        graph: A dictionary representing the graph where keys are nodes
               and values are lists of adjacent nodes
        start_node: The node to start BFS from
    
    Returns:
        A list containing the BFS traversal order
    """
    # Check if start_node exists in the graph
    if start_node not in graph:
        return []
    
    visited = set()
    queue = [start_node]
    traversal_result = []
    
    # Mark the start node as visited
    visited.add(start_node)
    
    while queue:
        # Dequeue a vertex from queue
        current_node = queue.pop(0)
        traversal_result.append(current_node)
        
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, mark it visited and enqueue it
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_result