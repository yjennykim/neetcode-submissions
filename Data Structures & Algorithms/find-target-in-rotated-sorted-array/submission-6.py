class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find pivot. Biggest L possible
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > nums[l]:
                l = m 
            else:
                r = m - 1
        
        if l == len(nums)-1:
            pivot = 0
        else:
            pivot = l+1

        # Go left of pivot or right, depending on target
        print("pivot", pivot)
        
        indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
        fixed = indexed_nums[pivot:] + indexed_nums[:pivot]
        print("fixed list", fixed)
        l, r = 0, len(fixed)-1
        while l <= r:
            m = (l + r) // 2
            if fixed[m][0] > target:
                r = m - 1
            elif fixed[m][0] < target:
                l = m + 1
            else:
                return fixed[m][1]
        
        return -1
