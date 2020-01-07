# 48.旋转图像
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
class Solution:
    # 方法 1 ：转置加翻转
    #
    # 最直接的想法是先转置矩阵，然后翻转每一行。这个简单的方法已经能达到最优的时间复杂度
    def rotate_image_one(self, matrix: list) -> list:
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
        return matrix

    # 方法 2 ：旋转四个矩形
    # https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode/
    def rotate_image_two(self, matrix: list) -> list:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row
        return matrix

    # 方法 3：在单次循环中旋转 4 个矩形
    # 该想法和方法 2 相同，但是所有的操作可以在单次循环内完成并且这是更精简的方法。
    def rotate_image_three(self, matrix: list) -> list:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        return matrix

s = Solution()
data = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# print(s.rotate_image_one(data))
# print(s.rotate_image_two(data))
print(s.rotate_image_three(data))