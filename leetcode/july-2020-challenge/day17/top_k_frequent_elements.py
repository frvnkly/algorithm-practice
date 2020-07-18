# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.


from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        
        f_arr = list()
        for f in freqs:
            f_arr.append([f, freqs[f]])
        
        left = 0
        right = len(f_arr) - 1
        while True:
            p = self.pivot(f_arr, left, right)
            
            if p < len(f_arr) - k:
                left = p + 1
            elif p > len(f_arr) - k:
                right = p - 1
            else:
                print(f_arr, p)
                out = list()
                for i in range(p, len(f_arr)):
                    out.append(f_arr[i][0])
                return out
            
    def pivot(self, arr, left, right):
        if left >= right:
            return left
        
        p = left
        i, j = left + 1, right
        while i < j:
            if arr[i][1] >= arr[p][1]:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
            else:
                i += 1
                
        if arr[p][1] <= arr[i][1]:
            arr[p], arr[i-1] = arr[i-1], arr[p]
            return i - 1
        else:
            arr[p], arr[i] = arr[i], arr[p]
            return i
        