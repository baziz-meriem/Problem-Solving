class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        ladder = dict()

        for j in range(n):
            for k in range(n):
                if board[j][k] != -1:
                    if (n - 1 - j) % 2 == 0:
                        num = k + 1
                    else:
                        num = n - k
                    num += (n - 1 - j) * n
                    ladder[num] = board[j][k]

        visited = [0 for j in range(target + 1)]
        visited[1] = 1
        curr = [1]
        steps = 0

        while curr:
            steps += 1
            new = set()
            for j in curr:
                if target - j <= 6:
                    return steps
                for k in range(j + 1, j + 7):
                    if k in ladder and (not visited[ladder[k]]):
                        if ladder[k] == target:
                            return steps
                        new.add(ladder[k])
                        visited[ladder[k]] = 1
                    elif k not in ladder and (not visited[k]):
                        new.add(k)
                        visited[k] = 1
            curr = new

        return -1