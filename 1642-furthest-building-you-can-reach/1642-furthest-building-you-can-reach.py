import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_jumps = []
        i = 0
        
        while i < len(heights)-1:
            gap= heights[i+1] - heights[i]
            if gap > 0:
                if ladders:
                
                    heapq.heappush(ladder_jumps,gap)
                    ladders -=1
                elif bricks:
                    if ladder_jumps and ladder_jumps[0] <= bricks:
                        if gap < ladder_jumps[0]:
                            bricks -= gap
                        else:
                            bricks-= heapq.heappop(ladder_jumps)
                            heapq.heappush(ladder_jumps,gap)
                    elif gap <= bricks:
                        bricks-= gap
                        
                    else:
                        return i
                else:
                    return i
            i+=1
        return i


        
        
#         jumps = []
#         j =0
#         while j < len(heights)-2:
            
#             jump = heights[j] - heights[j+1] 
#             if jump > 0:
#                 if jump < bricks:
#                     bricks -= jump
#                 elif ladders:
#                     ladders -= 1
#                 else:
#                     break
                
#             j += 1
#         return j
                
                
            
            