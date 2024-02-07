class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the shortest string in the list
        shortes_string = min(strs,key=len)
        common_prefix = ""
        #parcourir le mot car par car 
        for car in shortes_string:
            common_prefix = common_prefix + car
            #pour chaque pref si il est prefix de tout les mots de la liste
            for word in strs :
                if not word.startswith(common_prefix):
                    #retourner le prefixe deja exisitant
                        return common_prefix[:-1]

        return shortes_string
        