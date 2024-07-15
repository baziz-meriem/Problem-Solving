def chooseN(lst: tuple, n: int) -> Generator[tuple, None, None]:
    l_len = len(lst)
    
    def recurr(i: int=0, m: int=n) -> Generator[tuple, None, None]:
        if m == 0:
            yield ()
            return
        if l_len - i < m: return
        if l_len - i == m:
            yield lst[i:]
            return
        for ans in recurr(i + 1, m - 1):
            yield (lst[i], *ans)
        for ans in recurr(i + 1, m):
            yield ans
        return
    for ans in recurr():
        yield ans
    return

import heapq
from sortedcontainers import SortedList

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        shape = (len(grid), len(grid[0]))
        
        key_pos = {}
        for i, row in enumerate(grid):
            for j, l in enumerate(row):
                if l == "@": pos = (i, j)
                elif l.islower():
                    key_pos[l] = (i, j)
        keys = list(key_pos.keys())
        keys_dict = {k: i for i, k in enumerate(keys)}
        n_keys = len(keys)
        if n_keys == 0: return 0
        
        adjacency = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if abs(x + y) == 1}
        def adjacent(pos: Tuple[int], k_list: List[int]) -> Generator[Tuple[int], None, None]:
            for d in adjacency:
                pos2 = tuple(x + y for x, y in zip(pos, d))
                for p, s in zip(pos2, shape):
                    if not 0 <= p < s: break
                else:
                    l = grid[pos2[0]][pos2[1]]
                    if l == "#" or l.isupper() and keys_dict[l.lower()] in k_list:
                        continue
                    yield pos2
            return
    
        def distance(pos1: Tuple[int], pos2: Tuple[int]) -> int:
            return sum(abs(x - y) for x, y in zip(pos1, pos2))
        
        key_dists = [{(i,): 0} for i in range(n_keys)]
        for i in range(n_keys):
            p1 = key_pos[keys[i]]
            for j in range(i + 1, n_keys):
                p2 = key_pos[keys[j]]
                dist = distance(p1, p2)
                key_dists[i][(i, j)] = dist
                key_dists[j][(i, j)] = dist
        
        for length in range(3, n_keys + 1):
            for k_lst in chooseN(tuple(range(n_keys)), length):
                for ind, i in enumerate(k_lst):
                    k_lst2 = (*k_lst[:ind], *k_lst[ind + 1:])
                    ans = float("inf")
                    for j in k_lst2:
                        ans = min(ans, key_dists[i][tuple(sorted((i, j)))] + key_dists[j][k_lst2])
                    key_dists[i][k_lst] = ans

        def heuristic(pos: Tuple[int], k_list: List[int]) -> int:
            res = float("inf")
            k_list = tuple(k_list)
            for i in k_list:
                res = min(res, distance(pos, key_pos[keys[i]]) + key_dists[i][k_list])
            return res
        
        k_list = SortedList(range(n_keys))
        heap = [(heuristic(pos, k_list), 0, pos, k_list)]
        seen = set((pos, tuple(k_list)))
        while heap:
            neg_d, pos, k_list = heapq.heappop(heap)[1:]
            tup = (pos, tuple(k_list))
            if tup in seen: continue
            neg_d -= 1
            seen.add(tup)
            for pos2 in adjacent(pos, k_list):
                l = grid[pos2[0]][pos2[1]]
                if l in keys_dict.keys() and keys_dict[l] in k_list:
                    if len(k_list) == 1: return -neg_d
                    k_list2 = SortedList(k_list)
                    k_list2.remove(keys_dict[l])
                else: k_list2 = k_list
                heapq.heappush(heap, (heuristic(pos2, k_list2) - neg_d, neg_d, pos2, k_list2))
        return -1