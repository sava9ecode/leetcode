class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        vowels = "aeiouAEIOU"

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1

        return "".join(s)
