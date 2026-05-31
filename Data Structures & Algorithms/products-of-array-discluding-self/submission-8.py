class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = [] 

        product = 1
        # l - r
        for i in range(len(nums)):
            product *= nums[i]
            l.append(product)
        print("l", l)

        # r - l
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            r.append(product)
        
        r = r[::-1]
        print("r", r)
        
        if len(nums) == 1:
            return nums
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(r[i+1])
            elif i == len(nums) - 1:
                output.append(l[i-1])
            else:
                output.append(r[i+1] * l[i-1])
        
        return output



        
