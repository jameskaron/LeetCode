# 只出现一次的数字
class Solution:
    # 列表操作
    def singleNumber_one(self, nums: list) -> int:
        """
                :type nums: List[int]
                :rtype: int
                """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

    # 哈希表
    def singleNumber_two(self, nums: list) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    # 数学: 2(a+b+c)-(a+a+b+b+c)=c
    def singleNumber_three(self, nums: list) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    # 位操作:XOR a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b
    def singleNumber_four(self, nums: list) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


s = Solution()
# data = [2, 2, 1]
data = [4,1,2,1,2]
# resp = s.singleNumber_one(data)
# resp = s.singleNumber_two(data)
# resp = s.singleNumber_three(data)
resp = s.singleNumber_four(data)
print(resp)
