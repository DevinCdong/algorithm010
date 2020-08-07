class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        sarr = list(S)
        l, h = 0, len(sarr) - 1
        def is_char(c):
            return "a" <= c <= "z" or "A" <= c <= "Z"
        while l < h:
            while l < h and not is_char(sarr[l]):
                l += 1
            while l < h and not is_char(sarr[h]):
                h -= 1
            if l < h:
                sarr[l], sarr[h] = sarr[h], sarr[l]
                l += 1
                h -= 1
        return "".join(sarr)
