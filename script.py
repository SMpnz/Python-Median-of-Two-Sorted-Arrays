from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        if nums1 == []:
            return None
        elif nums1[0] == 0 and len(nums1) == 1:
            return 0 
        i = 0
        j = 0
        while i < len(nums1):
            j+=1
            i+=2
        if len(nums1) > 1:     
            if len(nums1)%2 == 0:
                return (nums1[j-1]+nums1[j])/2
            else:
                return nums1[j-1]         
        return nums1[0]

def main():
    """Проверка алгоритма"""
    ex_S = Solution()
    nums1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    nums2 =[0,6]
    print(ex_S.findMedianSortedArrays(nums1,nums2))
    nums1 = []
    nums2 = [1]
    print(ex_S.findMedianSortedArrays(nums1,nums2))

    nums1 = [1,3]
    nums2 = [2]
    print(ex_S.findMedianSortedArrays(nums1,nums2))

    nums1 = [1,2]
    nums2 = [3,4]
    print(ex_S.findMedianSortedArrays(nums1,nums2))

if __name__ == "__main__":
    main()



