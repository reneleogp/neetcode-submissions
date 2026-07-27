class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1     
        for i in range(len(arr) - 1, -1, -1):
            arr[i], biggest = biggest, max(arr[i], biggest)

        return arr
            
            