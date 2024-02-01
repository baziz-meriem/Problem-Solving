from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return["FizzBuzz" if (i+1)%3==0 and (i+1)%5==0 else "Fizz" if (i+1)%3==0 else "Buzz" if (i+1)%5==0 else str(i+1)  for i in range(n)]
