class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0 for _ in range(26)]
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        for char in t:
            char_count[ord(char) - ord('a')] -= 1
        return len(set(char_count)) == 1 and char_count[0] == 0