# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
class Solution:
    def plusOne(self, digits: list) -> list:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] is not 0:
                return digits
        digits = [0] * (len(digits) + 1)
        digits[0] = 1
        return digits


s = Solution()
# data = [1,2,3]
# data = [4,3,2,1]
data = [9]
# data = [1, 2, 3, 9]
print(s.plusOne(data))