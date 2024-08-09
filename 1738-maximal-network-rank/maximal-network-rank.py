from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = defaultdict(set)
        for a, b in roads:
            connections[a].add((a,b))
            connections[b].add((a,b))
        
        max_rank = 0
        
        # Compare all pairs of different cities
        for i in range(n):
            for j in range(i + 1, n):
                
                intersection_length = len(connections[i] & connections[j])
                network_rank = len(connections[i]) + len(connections[j]) - intersection_length
                max_rank = max(max_rank, network_rank)
        
        return max_rank
