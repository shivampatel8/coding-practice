# Add 2 numbers without using '+'
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b != 0:
          c = (a&b)
          a = (a^b)%MASK
          b = (c<<1)%MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

if __name__ == '__main__':
  print(Solution().getSum(-12,-8))