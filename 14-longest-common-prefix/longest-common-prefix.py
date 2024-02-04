class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cont=True
        prefix = ""
        shortest= min(strs,key=len) #finds shortest word in the list

        for char in shortest : #flow
            #add new char to prefix
            prefix += char #f
            
            for s in strs:
                if s[:len(prefix)] != prefix  :
                    cont=False
                    break; #no need to persue the search in the rest of the strings
            if not cont:
                prefix = prefix[:-1]
                break;    
                

        return prefix
        