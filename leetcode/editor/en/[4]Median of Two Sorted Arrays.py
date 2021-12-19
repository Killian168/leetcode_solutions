# leetcode submit region begin(Prohibit modification and deletion)
from sys import maxsize


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Search the shortest array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        start = 0
        end = nums1_len
        while start <= end:
            partition_nums1 = (start + end) // 2
            partition_nums2 = (nums1_len + nums2_len + 1) // 2 - partition_nums1

            # If there are no elements left on the left side after partition
            maxLeftNums1 = -maxsize if partition_nums1 == 0 else nums1[partition_nums1 - 1]

            # If there are no elements left on the right side after partition
            minRightNums1 = maxsize if partition_nums1 == nums1_len else nums1[partition_nums1]

            # Similarly for nums2
            maxLeftNums2 = -maxsize if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            minRightNums2 = maxsize if partition_nums2 == nums2_len else nums2[partition_nums2]

            # Check if we have found a match
            if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
                if (nums1_len + nums2_len) % 2 == 0:
                    return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2
                else:
                    return max(maxLeftNums1, maxLeftNums2)

            # If we are too far on the right, we need to go to left side
            elif maxLeftNums1 > minRightNums2:
                end = partition_nums1 - 1

            # If we are too far on the left, we need to go to right side
            else:
                start = partition_nums1 + 1
# leetcode submit region end(Prohibit modification and deletion)