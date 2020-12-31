# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 示例 2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#  
#
# 提示：
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_len = len(digits)
        for i in range(list_len-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        digits = [0 for i in range(list_len+1)]
        digits[0] = 1
        print(digits)
        return digits


if __name__ == '__main__':
    s = Solution()
    digits_1 = [1, 2, 3]
    digits_2 = [4, 3, 2, 1]
    digits_3 = [1, 9, 9, 9]
    digits_4 = [9]
    # assert s.plusOne(digits_1) == [1, 2, 4]
    # assert s.plusOne(digits_2) == [4, 3, 2, 2]
    # assert s.plusOne(digits_3) == [2, 0, 0, 0]
    assert s.plusOne(digits_4) == [1, 0]
