class Solution:

    '''
    Example 1.
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    '''

    '''
    Example 2
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    '''

    # brute force
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if Solution.is_unique(s, i, j):
                    max_length = max(max_length, j - i)
        return max_length
    
    @staticmethod
    def is_unique(s: str, start: int, end: int) -> bool:
        char_set = set()
        for i in range(start, end):
            if s[i] in char_set:
                return False
            char_set.add(s[i])
        return True

    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        n = len(s)
        char_index = {} # A dictionary to store character indices
        max_length = 0
        left, right = 0, 0

        while right < n:
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length

solution = Solution()
result1 = solution.lengthOfLongestSubstring("abcabcbb")
result2 = solution.lengthOfLongestSubstringSlidingWindow("abcdabctyuiobb")
print(result1)
print(result2)
