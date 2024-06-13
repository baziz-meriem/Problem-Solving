class Solution:
      def findCenter(self, edges: List[List[int]]) -> int:
        ad = defaultdict(list)
        for i in edges:
            ad[i[0]].append(i[1])
            ad[i[1]].append(i[0])
        x = len(ad)
        print(x)
        maxi = 0
        for i,j in ad.items():
            if len(j)==x-1:
                return i