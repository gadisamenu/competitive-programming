class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # added = numbers[0] + numbers[1]
        length = len(numbers)
        i = 0
        j = length -1
        
        while i<j:
            added = numbers[i] + numbers[j]
            if added == target:
                return [i+1,j+1]
            elif added < target:
                i +=1
            else:
                j -=1
        return[]