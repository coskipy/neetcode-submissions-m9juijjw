class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        product = 1
        output = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeros.append(i)

            if len(zeros) == 2:
                return [0]*len(nums)

            if nums[i] != 0:
                product *= nums[i]
                
        print(product, zeros)

        if len(zeros) == 0:
            for num in nums:
                output.append(int(product/num))

        # else 1 zero
        else :
            for i in range(0, len(nums)):
                if i not in zeros:
                    output.append(0)
                else:
                    output.append(product)

        return output
