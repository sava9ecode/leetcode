from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for n in arr:
            d[n] += 1
        check = set()
        for val in d.values():
            if val in check:
                return False
            check.add(val)
        return True
