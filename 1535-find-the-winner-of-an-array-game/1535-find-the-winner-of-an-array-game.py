class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_win_count = 0
        winner = arr[0]
        for idx in range(1,len(arr)):
            if max_win_count == k:
                return winner
            if arr[idx] < winner:
                max_win_count += 1
            else:
                max_win_count = 1
                winner = arr[idx]
                
        return winner
                
        