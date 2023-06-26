class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        first_pointer, second_pointer = 0, 0
        while first_pointer < len(s) and second_pointer < len(t):
            if s[first_pointer] == t[second_pointer]:
                first_pointer += 1
                second_pointer += 1
            else:
                second_pointer += 1
        return first_pointer == len(s)