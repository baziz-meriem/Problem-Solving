class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        X = sum(1 if "+" in o else -1 for o in operations)
        return X
        