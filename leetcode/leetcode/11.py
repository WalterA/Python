class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) -1
        max_area = 0
        while left_pointer < right_pointer:
            
            width = right_pointer - left_pointer
            current_area = min(height[left_pointer], height[right_pointer]) * width
            max_area = max(current_area, max_area)
            
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area