class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out =""
        idx1=0
        idx2=0
        idx = 0 
        (long,short) = (word1,word2) if len(word1)>=len(word2) else (word2,word1)
        
        #check if the length of the smallest string is reached
        while idx <2*(len(short)):
            if idx%2==0:
                out = out+word1[idx1] 
                idx1 +=1
            else:
                out = out+word2[idx2] 
                idx2 +=1
            idx +=1
        #concatenate the rest of the long word
        if(len(long)>len(short)):
            out = out+long[len(short):]
            
        return out


