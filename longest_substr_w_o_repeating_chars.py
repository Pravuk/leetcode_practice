class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 1
        left = 0
        charts = set()
        for right in range(len(s)):
            if s[right] not in charts:
                max_count = max(max_count, right - left + 1)
            else:
                while s[right] in charts:
                    charts.remove(s[left])
                    left += 1
            charts.add(s[right])
        return max_count


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
