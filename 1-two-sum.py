
# https://leetcode.cn/problems/two-sum/

# 两个数之和 -第一映像
def two_sum_v1(nums, target):
    for i_index,i_item in enumerate(nums):
        for j_index,j_item in enumerate(nums):
            if i_item+j_item  == target and i_index != j_index:
                return [i_index, j_item]


# - 优化
def two_sum_v2(nums,target):
    for i_index,i in enumerate(nums):
        for j_index,j in enumerate(nums[i_index+1:]):
            if i+j == target:
                return [i_index, j_index+i_index+1]

