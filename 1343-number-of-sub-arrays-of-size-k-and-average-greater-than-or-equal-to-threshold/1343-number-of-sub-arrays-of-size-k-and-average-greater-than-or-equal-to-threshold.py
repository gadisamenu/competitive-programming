class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        _sum = 0
        for i in range(k):
            _sum += arr[i]
           
        ans = 0
        i = 0
        j = k-1
        while True:
            if _sum // k >= threshold:
                ans += 1
                
            _sum -= arr[i]
            i+=1
            j += 1
            if j >= len(arr):break
            _sum += arr[j]
            
        return ans