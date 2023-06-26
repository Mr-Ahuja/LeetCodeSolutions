class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_greatest = -1
        for index in range(len(arr) - 1, -1, -1):
            arr[index], current_greatest = current_greatest, max(current_greatest, arr[index])
        return arr
            