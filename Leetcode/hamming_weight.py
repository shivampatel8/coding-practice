#Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        print(binary)
        x = 1
        count = 0
        while n!=0:
          a = n ^ x
          x = x<<1
          if a>=n:
            continue
          if n!=a:
            count+=1
          n = a
        return count

if __name__ == '__main__':
  print(Solution().hammingWeight(15))