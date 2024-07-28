from collections import Counter
class Solution:
     
    def findCenter(self,edges):
        # Flatten the edge list into a single list of nodes
        flattened_nodes = [node for edge in edges for node in edge]

        # Count occurrences of each node
        node_counts = Counter(flattened_nodes)

        # The center node will have a count of n-1 (where n is the number of nodes)
        n = len(edges) + 1
        for node, count in node_counts.items():
            if count == n - 1:
                return node
