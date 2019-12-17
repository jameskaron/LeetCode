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