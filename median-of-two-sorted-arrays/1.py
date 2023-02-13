'''
# O(n + m) Solution
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
'''
# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2511/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms/?orderBy=most_votes&languageTags=python

class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
    
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
