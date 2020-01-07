# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

class Solution:
    # 双指针
    def reverseString_one(self, s: list) -> list:
        # 两个指针要同时移动
        e_idx = len(s)-1
        for f_idx in range(int(len(s)/2)):
            print("front index: " + s[f_idx])
            print("end index: " + s[e_idx])
            temp = s[e_idx]
            s[e_idx] = s[f_idx]
            s[f_idx] = temp
            e_idx -= 1
        return s

    def reverseString_two(self, s: list) -> list:
        s.reverse()
        return s

    # 递归
    def reverseString_three(self, s: list) -> list:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s)-1)
        return s


s = Solution()
str1 = ["h","e","l","l","o"]
str2 = ["H","a","n","n","a","h"]
# print(s.reverseString(str1))
# print(s.reverseString_one(str2))
# print(s.reverseString_two(str2))
print(s.reverseString_three(str2))