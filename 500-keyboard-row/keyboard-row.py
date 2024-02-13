class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        possible_words = []

        for w in words:
            row = "qwertyuiop" if w[0].lower() in "qwertyuiop" else "asdfghjkl" if w[0].lower() in "asdfghjkl" else "zxcvbnm"
            possible_words.append(w)
            for car in w[1:]:
                if car.lower() not in row:
                    possible_words.remove(w)
                    break;
                

        return possible_words
