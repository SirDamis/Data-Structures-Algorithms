class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s =sorted(s)
        # t =sorted(t)
        # return s == t

        dicts = {}
        for item in s:
            dicts[item] = dicts.get(item, 0) + 1
        for item in t:
            if item not in dicts:
                return False
            dicts[item] -= 1
        for item in dicts:
            if dicts[item] != 0: return False
        return True
