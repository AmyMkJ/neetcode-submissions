class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        reverse_s = s[::-1]
        
        return s == reverse_s