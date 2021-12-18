# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) == 0:
            return 0

        last_indexs = dict()
        max_len = 0
        start_index = 0

        for i in range(len(string)):
            if string[i] in last_indexs:
                start_index = max(start_index, last_indexs[string[i]] + 1)

            max_len = max(max_len, i - start_index + 1)
            last_indexs[string[i]] = i

        return max_len
# leetcode submit region end(Prohibit modification and deletion)
