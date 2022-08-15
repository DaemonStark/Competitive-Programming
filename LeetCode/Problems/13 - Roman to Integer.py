class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        # Length of the given string
        n = len(s)
        # Storing last val
        num = roman_dict[s[n - 1]]
        # Loop for each character from right to left
        # Going in reverse
        # Starting from the second last element i.e n-2
        for i in range(n - 2, -1, -1):
            # Check if the character at right of current character is bigger or smaller
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                num += roman_dict[s[i]]
            else:
                num -= roman_dict[s[i]]
        return num
