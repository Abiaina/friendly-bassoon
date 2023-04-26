class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_length = 0
        for i in s:
            if i not in substring:
                substring += i
            else:
                while i in substring:
                    substring = substring[1:]
            if max_length < len(substring):
                max_length = len(substring)
        return max_length


test = Solution()
print(test.lengthOfLongestSubstring("Hello world this is me"))
