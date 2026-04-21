class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1   # add 1 if last bit is 1
            n >>= 1          # shift right to check next bit
        return count