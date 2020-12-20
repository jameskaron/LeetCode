# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

class Solution(object):
    # index
    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ""

        prefix = strs[0]
        for k in strs[1:]:
            while True:
                try:
                    k.index(prefix)
                    break
                except:
                    if len(prefix) == 0:
                        return ""
                    prefix = prefix[:len(prefix) - 1]
        return prefix


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    strs1 = ["dog", "racecar", "car"]
    strs2 = ["c", "acc", "ccc"]
    # assert s.longestCommonPrefix(strs) == 'fl'
    # assert s.longestCommonPrefix(strs1) == ''
    # TODO: error
    assert s.longestCommonPrefix(strs2) == ''


