# 方法 1：暴力
# 最简单的方法是旋转 k 次，每次将数组旋转 1 个元素。
def rotate_one(nums: list, k: int) -> list:
    for i in range(k):
        previous = nums[len(nums) - 1]
        for j in range(len(nums)):
            temp = nums[j]
            nums[j] = previous
            previous = temp
    return nums

# 方法 2：使用额外的数组
# 我们可以用一个额外的数组来将每个元素放到正确的位置上，也就是原本数组里下标为 ii 的我们把它放到 (i+k)%数组长度(i+k)%数组长度 的位置。然后把新的数组拷贝到原数组中。
def rotate_two(nums: list, k: int) -> list:
    a = [0] * len(nums)
    for i in range(len(nums)):
        last_index = (i + k) % len(nums)
        a[last_index] = nums[i]
    for i in range(len(nums)):
        nums[i] = a[i]
    return nums

# Bug!
# 方法 3：使用环状替换
# def rotate_three(nums: list, k: int) -> list:
#     k = k % len(nums)
#     count = 0
#     for start in range(len(nums)):
#         current = start
#         prev = nums[start]
#         while True:
#             next_item = (current + k) % len(nums)
#             temp = nums[next_item]
#             nums[next_item] = prev
#             prev = temp
#             current = next_item
#             count += 1
#             if start != current:
#                 break
#     return nums

def rotate_four(nums: list, k: int) -> list:
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums

def reverse(nums: list, start: int, end: int):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1


origin_list = [1, 2, 3, 4, 5, 6, 7]
# origin_list_3 = [1, 2, 3, 4, 5, 6]
# print(rotate_one(origin_list, 3))
# print(rotate_two(origin_list, 3))
# origin_list = [-1, -100, 3, 99]
# print(rotate(origin_list, 2))
print(rotate_four(origin_list, 3))
