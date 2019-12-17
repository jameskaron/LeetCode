# 给定两个数组，编写一个函数来计算它们的交集
class Solution:
    # 解法一：哈希表
    def intersect_one(self, nums1: list, nums2: list) -> list:
        ints = {}
        res = []
        for i1 in nums1:
            if i1 in ints:
                ints[i1] += 1
            else:
                ints[i1] = 1
        print(ints)

        for i2 in nums2:
            if i2 in ints:
                res.append(i2)
                if ints[i2] > 1:
                    ints[i2] -= 1
                else:
                    del ints[i2]
        return res

    # 解法二：双指针
    def intersect_two(self, nums1: list, nums2: list) -> list:
        list.sort(nums1)
        list.sort(nums2)
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res


s = Solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums2 = [4,9,5]
nums1 = [9,4,9,8,4]
print(s.intersect_two(nums1, nums2))