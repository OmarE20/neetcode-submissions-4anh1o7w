class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string (only keep letters and numbers)
        cleaned = []
        for i in s:
            if i.isalnum():
                cleaned.append(i.lower())
        
        # Create a left and right side, increment both until you reach the middle. If the left doesn't equal the right at any time, return false
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True