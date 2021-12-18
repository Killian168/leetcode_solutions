
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()

        for index, number in enumerate(nums):
            magic_number = target - number
            magic_number = nums_map.get(magic_number, None)
            if magic_number is not None:
                return [magic_number, index]
            else:
                nums_map[number] = index

# leetcode submit region end(Prohibit modification and deletion)
