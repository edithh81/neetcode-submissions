class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1
        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n 
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left += 1
            else:
                right -=1


        return False