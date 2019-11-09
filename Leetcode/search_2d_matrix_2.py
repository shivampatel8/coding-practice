# 240. Search a 2D Matrix II
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        found = False
        i = len(matrix)-1
        j = 0
        while i>0 and j<=len(matrix[0])-1:
          if target<matrix[i][j]:
            i -= 1
          elif target>matrix[i][j]:
            j += 1
          else:
            return True
        return False

    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j == target:
                    return True
        return False
if __name__ == '__main__':
  print(Solution().searchMatrix([[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 31))