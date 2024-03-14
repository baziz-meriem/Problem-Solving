class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #sort players reverse
        players.sort()
        #sort trainers 
        trainers.sort()

        idx_trainers=0
        idx_players=0
        max=0

        while idx_players < len(players) and idx_trainers < len(trainers):
            if players[idx_players]<= trainers[idx_trainers]:
                idx_trainers += 1
                idx_players += 1
                max += 1
            else:
                idx_trainers += 1
        return max

