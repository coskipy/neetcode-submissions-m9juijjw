class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Cum product approach

        ltr_product = [nums[0]]
        for i in range(1, len(nums)):
            ltr_product.append(nums[i]*ltr_product[i-1])
        
        # Flip list for easy comprehension
        rev_nums = nums[::-1]
        rtl_product = [rev_nums[0]]
        for i in range(1, len(rev_nums)):
            rtl_product.append(rev_nums[i]*rtl_product[i-1])
        rtl_product = rtl_product[::-1]

        #print(ltr_product, rtl_product)
        output = []
        for i in range(0, len(nums)):
            #print(i, ltr_product[i], rtl_product[i])
            if i == 0:
                output.append(rtl_product[1])
            elif i == len(nums) - 1:
                output.append(ltr_product[len(nums) - 2])
            else:
                output.append(int(ltr_product[i-1] * rtl_product[i+1]))

        return output