class Solution:
    def isPalindrome(self, s: str) -> bool:
        base = ''
        for char in s:
            if char.isalnum() == True:
                base += char

        base = base.lower()
        if base == base[::-1]:
            return True
        
        return False