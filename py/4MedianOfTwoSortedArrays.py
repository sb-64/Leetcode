class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        combined_nums: list[int] = sorted(nums1 + nums2)
        midpoint: float = ((len(combined_nums) + 1) / 2) - 1 

        if len(combined_nums) % 2 != 0:
            return combined_nums[int(midpoint)] # subtract 1 to map it to python index
        else:
            left_el, right_el = combined_nums[int(midpoint-0.5)], combined_nums[int(midpoint+0.5)] 
            return (left_el + right_el) / 2
 


        


if __name__ == '__main__':
    sol = Solution()
    
    nums1, nums2 = [1, 3], [2]
    print(sol.findMedianSortedArrays(nums1, nums2))
    nums1, nums2 = [1, 2], [3, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))
