# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# s = "leetcode" 返回 0.
# s = "loveleetcode", 返回 2.
import collections

class Solution:
    # 方法一： 线性时间复杂度解法
    def firstUniqChar_one(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


s = Solution()
data = "leetcode"
data_1 = "loveleetcode"
data_2 = "llmm"
data_3 = "aadadaad"
# print(s.firstUniqChar(data))
print(s.firstUniqChar_one(data_3))
