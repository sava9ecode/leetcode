class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        cnt = sum([s[i] in vowels for i in range(k)])
        ans = cnt
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels)
            cnt -= int(s[i - k] in vowels)
            ans = max(ans, cnt)
            if ans == k:
                break
        return ans
