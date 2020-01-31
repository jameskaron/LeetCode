# 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转

class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x))
        l.reverse()
        if l[len(l)-1] is "-":
            symbol = l.pop(len(l)-1)
            l.insert(0, symbol)
        result = int("".join(l))
        floor = -2**31
        upper = 2**31 - 1
        if floor <= result <= upper:
            return result
        else:
            return 0


s = Solution()
data = 123
data_1 = -123
data_2 = 120
data_3 = 1534236469
assert s.reverse(data) == 321
assert s.reverse(data_1) == -321
assert s.reverse(data_2) == 21
assert s.reverse(data_3) == 0

# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0
