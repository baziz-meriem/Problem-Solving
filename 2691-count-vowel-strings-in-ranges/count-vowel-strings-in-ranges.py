class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        final_queries_list=[]

        pref_sum=[1 if words[0][0] in "aeiou" and words[0][-1] in "aeiou" else 0]
        for idx in range(1,len(words)):
            value = 1 if words[idx][0] in "aeiou" and words[idx][-1] in "aeiou" else 0
            pref_sum.append(pref_sum[-1]+ value )
       

        for s_query,e_query in queries:
            if s_query >0:
                diff = pref_sum[e_query] - pref_sum[s_query-1]
            else:
                diff = pref_sum[e_query]

            final_queries_list.append(diff)
        return final_queries_list