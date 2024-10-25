# class Solution:
# Helper method to perform DFS using Tarjan's algorithm
def dfs( graph, currentNode, parent, currentTime, discoveryTime, lowestTime, isInfected, malwareSpreadCount):
    # Initialize discovery and lowest reachable time for the current node
    lowestTime[currentNode] = discoveryTime[currentNode] = currentTime
    isMalwareSpread = isInfected[currentNode]
    componentSize = 1  # Initialize component size

    # Traverse all connected nodes
    for neighbor in range(len(graph[currentNode])):
        if graph[currentNode][neighbor] == 1:  # Check if there is a connection
            if discoveryTime[neighbor] == 0:  # If the neighbor has not been visited
                print(f"dfs traversal for child: {neighbor}")
                subTreeSize = dfs(graph, neighbor, currentNode, currentTime + 1, discoveryTime, lowestTime, isInfected, malwareSpreadCount)
                print(f"subTreeSize  : {subTreeSize }")
                if subTreeSize == 0:  # If subtree contains a malware node
                    isMalwareSpread = True
                else:
                    componentSize += subTreeSize  # Add subtree size to the current component size
                # Update malware spread count if the lowest time of the neighbor is greater than or equal to the discovery time
                print(f"neighbor: {neighbor} currentnode: {currentNode}")
                if lowestTime[neighbor] >= discoveryTime[currentNode]:
                    malwareSpreadCount[currentNode] += subTreeSize
                print(f"malwareSpreadCount[{currentNode}]: {malwareSpreadCount[currentNode]}")
                lowestTime[currentNode] = min(lowestTime[currentNode], lowestTime[neighbor])  # Update lowest reachable time
                print(f"lowestTime[{currentNode}] : {lowestTime[currentNode]} ")
            elif neighbor != parent:  # If the neighbor is not the parent, update the lowest reachable time
                lowestTime[currentNode] = min(lowestTime[currentNode], discoveryTime[neighbor])

    return 0 if isMalwareSpread else componentSize  # Return the size of the component if malware doesn't spread

def minMalwareSpread( graph, initial):
    numNodes = len(graph)  # Number of nodes in the graph
    nodeToRemove = initial[0]  # Start with the first node in the initial array
    maxSavedNodes = 0  # Maximum number of saved nodes

    isInfected = [False] * numNodes
    for node in initial:
        isInfected[node] = True  # Mark initially infected nodes

    discoveryTime = [0] * numNodes
    lowestTime = [0] * numNodes
    malwareSpreadCount = [0] * numNodes

    # Perform DFS for each initially infected node
    for node in initial:
        if discoveryTime[node] == 0:
            print(f"DFS TRAVERSAL STARTS for node: {node}")
            dfs(graph, node, -1, 1, discoveryTime, lowestTime, isInfected, malwareSpreadCount)
        # Choose the node that maximizes the number of saved nodes
        print(f"malwareSpreadCount:  {malwareSpreadCount}")
        print(f"malwareSpreadCount[{node}]  : {malwareSpreadCount[node]} ,maxSavedNodes : {maxSavedNodes} nodeToRemove :{nodeToRemove} ")
        if malwareSpreadCount[node] > maxSavedNodes or (malwareSpreadCount[node] == maxSavedNodes and node < nodeToRemove):
            maxSavedNodes = malwareSpreadCount[node]
            nodeToRemove = node

    return nodeToRemove


# Main method for testing
# if __name__ == "__main__":
    # solution = Solution()

# graph1 = [
#     [1, 0, 1],
#     [0, 1, 1],
#     [1, 1, 1]
# ]
# initial1 = [0, 2]
# print("Result for Example 1:", minMalwareSpread(graph1, initial1))
#
graph2 = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
initial2 = [1, 2]
print("Result for Example 2:", minMalwareSpread(graph2, initial2))

# graph3 = [
#     [1, 0, 0, 1],
#     [0, 1, 1, 0],
#     [0, 1, 1, 1],
#     [1, 0, 1, 1]
# ]
# initial3 = [0, 2]
# print("Result for Example 3:", minMalwareSpread(graph3, initial3))
