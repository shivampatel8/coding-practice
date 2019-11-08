class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string = bin(n)[2:]
        while len(string)<32:
            string = '0'+string
        string = string[::-1]
        return int(string,2)