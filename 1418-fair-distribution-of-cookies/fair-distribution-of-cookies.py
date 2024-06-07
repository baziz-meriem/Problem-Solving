class Solution:
    def distributeCookies(self, cookies, k):
        
        def backtrack(i, distribution, min_max_unfairness):
            if i == len(cookies):
                # Calculate the current maximum cookies any child has
                current_unfairness = max(distribution)
                # Update the minimum of these maximums
                return min(min_max_unfairness, current_unfairness)
            
            # Explore all possible ways to distribute the current bag of cookies
            local_min = float('inf')
            for child in range(k):
                distribution[child] += cookies[i]
                # Continue only if this distribution might lead to a new minimum
                if distribution[child] < min_max_unfairness:
                    result = backtrack(i + 1, distribution, min_max_unfairness)
                    local_min = min(local_min, result)
                distribution[child] -= cookies[i]
                # If this child had no cookies before this point, all subsequent children are also empty
                if distribution[child] == 0:
                    break

            return local_min

        # Initialize the distribution list and minimum maximum unfairness
        distribution = [0] * k
        min_max_unfairness = float('inf')
        # Start backtracking from the 0th cookie and an empty distribution
        return backtrack(0, distribution, min_max_unfairness)