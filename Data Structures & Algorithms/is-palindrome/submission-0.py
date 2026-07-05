class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for character in s:
            if character.isalnum():
                string+=character.lower()
        print(string)
        return string == string[::-1]
        