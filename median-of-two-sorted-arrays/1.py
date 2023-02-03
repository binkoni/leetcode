import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = k = 0
        n = len(nums1)
        m = len(nums2)
        nums3 = [0] * (n + m)

        while k < n + m:
            if i < n and j < m:
                if nums1[i] <= nums2[j]:
                    nums3[k] = nums1[i]
                    i += 1
                else:
                    nums3[k] = nums2[j]
                    j += 1
            elif i < n:
                nums3[k] = nums1[i]
                i += 1
            elif j < m:
                nums3[k] = nums2[j]
                j +=1
            k +=1

        return (nums3[math.floor((n + m) / 2)] + nums3[math.floor((n + m - 1) / 2)]) / 2
