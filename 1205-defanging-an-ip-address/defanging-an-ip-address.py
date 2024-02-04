class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join(["[.]" if n == "."  else n for n in address ])