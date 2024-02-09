class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses_dict = {}
        for winner,loser in matches:
            if winner not in loses_dict.keys():
                loses_dict[winner] = 0
            if loser not in loses_dict.keys():
                loses_dict[loser]  = 1
            elif loser in loses_dict.keys():
                loses_dict[loser]  += 1

        winners = []
        losers = []

        for element in loses_dict.items():
            if element[1] == 0:
                winners.append(element[0])
            elif element[1] == 1:
                losers.append(element[0])

        return [sorted(winners),sorted(losers)]

        