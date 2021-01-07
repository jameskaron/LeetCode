# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 一行不需要处理
        if numRows < 2:
            return s
        # 初始化数组,大小为行数
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            # 把单个字符输入到数组, 例如: 第0个字符,输入到数组[0]中;第1个字符,输入到数组[1]中;
            res[i] += c
            # 关键步骤: 折返. 到底(numRows-1)后,从大到小(数组[2]->数组[0])输入字符;到顶后相反(数组[0]->数组[2])
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return "".join(res)


if __name__ == '__main__':
    so = Solution()
    s = "LEETCODEISHIRING"
    # assert so.convert(s, numRows=3) == "LCIRETOESIIGEDHN"
    assert so.convert(s, numRows=4) == "LDREOEIIECIHNTSG"
