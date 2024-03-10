class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0

        sum_skill = skill[0] + skill[len(skill)-1]

        for idx in range(len(skill)//2):
            current_sum_skill = skill[idx] + skill[len(skill)-idx-1]
            if current_sum_skill != sum_skill:
                return -1
            else:
                chemistry += skill[idx] * skill[len(skill)-idx-1]
            idx += 1
        return chemistry

            

