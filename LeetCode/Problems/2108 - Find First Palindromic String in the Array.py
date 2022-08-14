class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for each in words:
            palString = [*each][::-1]
            if(list(each)==palString):
                return each
        return ""
