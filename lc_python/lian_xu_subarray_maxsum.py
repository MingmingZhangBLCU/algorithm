'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
'''

# 动态规划 O(n)  O(1)
#f(i):i号位置结束的最大和  f(i) =  max{f(i-1)+num_i ,num_i}

def maxSubArray(nums) -> int:
    max_num = -1000
    pre = 0
    for i in range(len(nums)):
        pre = max(pre+nums[i],nums[i]) #pre 表示 f(i-1)
        if pre > max_num:
            max_num = pre
    return max_num

# 分治法 O(nlogn)
# 左边存在最大
# 右边存在最大
#  横跨中间最大
def maxSubArray2(nums) -> int:
    def cross_max(left,right):
        if left == right:
            return nums[left]
        mid = (left + right)//2
        left_max , right_max = -1000,-1000
        count = 0
        for i in range(mid,left-1,-1):
            count += nums[i]
            if count > left_max:
                left_max = count
        count = 0
        for i in range(mid+1, right + 1):
            count += nums[i]
            if count > right_max:
                right_max = count
        return max(left_max,right_max,left_max + right_max)
    def helper(left,right):
        if left == right:
            return nums[left]
        mid = (left + right)//2
        left_max = helper(left,mid)
        rigt_max = helper(mid+1,right)
        mid_max = cross_max(left,right)
        return max(left_max,rigt_max,mid_max)
    return helper(0,len(nums)-1)
nums = [-2,1,-3,4,-1,2,-1,4]
print(maxSubArray2(nums))

#分治法 + 线段树
