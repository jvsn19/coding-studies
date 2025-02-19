class Solution:
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(heights) - 1
        max_left, max_right = heights[0], heights[~0]
        volume = 0

        while left < right:
            if heights[left] < heights[right]:
                volume += (max_left - heights[left])
                left += 1
                max_left = max(max_left, heights[left])
            else:
                volume += (max_right - heights[right])
                right -= 1
                max_right = max(max_right, heights[right])

        return volume