class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, shift = len(nums), nums.index(0)
        ring = lambda k: nums[(shift + k) % n]  # the circle, read from 0
        if all(ring(k) == k for k in range(n)):  # counts up along the arrow
            return min(shift, n - shift + 2)  # walk ahead, or turn, walk back, turn back
        if all(ring(k) == -k % n for k in range(n)):  # counts up against the arrow
            return min(shift + 2, n - shift)  # walk ahead and turn, or turn and walk back
        return -1