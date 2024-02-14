class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves_list  = []
        moves = 0
        for i,box in enumerate(boxes):#"--->110"
            for idx in range(len(boxes)):#"1-->10"
                if boxes[idx]=="1" and i!=idx:
                    moves += abs(int(i)-int(idx)) 
                    
            moves_list.append(moves)
            moves = 0

        return moves_list
        