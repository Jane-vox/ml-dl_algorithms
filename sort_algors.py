
class Solution:
    def Partition(self, nums, low, high):
        key = nums[low]  # 元素copied, nums[low]空了出来
        while low < high:
            while low < high and nums[high] >= key:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= key:
                low += 1
            nums[high] = nums[low]
        # 完成了一趟排序，pivot key 左边的小于都小于等于它，右边的大于等于它
        nums[low] = key
        return low  # 此时的low代表的是key的位置（有序分界点）

    # 1. 快速排序（递归分治法），每次能确定一个元素的位置，我使用的 key默认是最左边的值
    def QuickSort(self, nums, low, high):
        if low < high:  # 递归终止条件：Low==high
            pivot_loci = self.Partition(nums, low, high)

            # 再对左边进行sort
            self.QuickSort(nums, low, pivot_loci - 1)   # [low, key-1]
            # 再对右边进行sort
            self.QuickSort(nums, pivot_loci + 1, high)  # [key+1, high]
        return nums

    # 2. 冒泡排序实现
    def BubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            # 最后 i 个元素已经是排好序的!!!
            for j in range(0, n - i - 1):
                # 如果当前元素大于下一个元素，则交换它们
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


    # 3. 归并排序实现
    def MergeSort(self, nums):
        # 递归终止条件：数组长度为1或0
        if len(nums) <= 1:
            return nums
        # 分割步骤：找到中间点，分割数组
        mid = len(nums) // 2
        left = self.MergeSort(nums[:mid])  # 递归排序左半部分
        right = self.MergeSort(nums[mid:])  # 递归排序右半部分

        # 合并步骤：合并两个已排序的子数组
        return self.Merge(left, right)

    def Merge(self, left, right):
        merged = []
        i = j = 0
        # 比较两个数组的元素，依次将较小的元素加入结果数组
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # 将剩余元素添加到结果数组中
        merged.extend(left[i:])  # 列表中加入数组，用extend！！不是append！！
        merged.extend(right[j:])

        return merged


solution = Solution()
nums = [5, 1, 13, 2, 7, 0]
low = 0
high = len(nums) - 1
print(solution.QuickSort(nums, low, high))
print(solution.BubbleSort(nums))
print(solution.MergeSort(nums))
