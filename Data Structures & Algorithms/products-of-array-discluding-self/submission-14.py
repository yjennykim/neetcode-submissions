class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,4,6]
        '''
        # O(N^2) solution
        # res = []
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             total *= nums[j]
        #     res.append(total)
        # return res
        
        forward = []
        backward = []
        total_fwd = 1
        total_bwd = 1
        for i in range(len(nums)):
            total_fwd *= nums[i]
            forward.append(total_fwd)
            total_bwd *= nums[len(nums)-i-1]
            backward.append(total_bwd)
        
        backward = backward[::-1]

        res = []
        print('input', nums)
        print('fwd', forward)
        print('bwd', backward)

        
        for i in range(len(nums)):
            fwd_multiple = 1
            bwd_multiple = 1

            if i > 0:
                fwd_multiple = forward[i-1]

            if i < len(nums)-1:
                bwd_multiple = backward[i+1]

            res.append(fwd_multiple * bwd_multiple)
            '''
            [1,2,4,6]

            fwd: [1, 2, 8, 48]
            bwd: [48,48,24,6]
            '''
            
        return res
