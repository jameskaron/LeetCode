# 方法：双指针法
def remove_duplicates(nums: list) -> list:
    i = 0
    res = [nums[i]]
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            result.append(nums[i])
    return result


test_list = [1, 1, 2]

result = remove_duplicates(test_list)
print(result)

