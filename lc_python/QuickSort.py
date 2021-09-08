#交换排序之 快速排序
# 平均 O(nlogn)
#不稳定
nums =[5,6,3,2,1]
'''
def partsort(nums,left,right):
    '#左右指针占位法 还可用左右指针交换法 但不适用于链表'
    index = random.randint(left, right)
    nums[index], nums[right] = nums[right], nums[index]
    key = nums[right]
    while left < right:
        while left<right and nums[left] <= key :
            left += 1
        nums[right] = nums[left]
        while left<right and nums[right] >= key :
            right -= 1
        nums[left] = nums[right]
    nums[right] = key
    return right
'''
def partsort(nums,left,right): #pre 从哪开始大于基准  #cur 当前状态  适用于链表结构
    key = nums[right]
    pre,cur = left-1,left
    while cur < right :
        if  nums[cur] <= key:
            if cur - pre > 1:
                pre += 1
                tmp = nums[cur]
                nums[cur] = nums[pre]
                nums[pre] = tmp
            else:
                pre += 1
        cur += 1
    pre += 1
    nums[right] = nums[pre]
    nums[pre] = key
    return pre

def quicksort(nums,left,right):  #[0,n-1]
    if right <= left:
        return
    index = partsort(nums,left,right)   #选择一个基准 并将 大于其的放左边  小于其的放右边
    quicksort(nums,0,index-1)
    quicksort(nums, index + 1,right)
    # 快排右
quicksort(nums,0,len(nums)-1)
print(nums)

##############################
#非递归
nums =[5,6,3,2,1]
def quicksortNR(nums):
    stack = [(0,len(nums) - 1)]
    while len(stack):
        (left,right) = stack.pop()
        index = partsort(nums,left,right)
        if left < index-1:
            stack.append((left,index-1))
        if right > index + 1:
            stack.append((index+1,right))
quicksortNR(nums)
print(nums)