class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = [ch.lower() for ch in s if ch.isalnum()]

        return filtered_string == filtered_string[::-1]