class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        queue = deque([deck.pop()])
        
        while deck:
            last = queue.pop()
            
            queue.appendleft(last)
            queue.appendleft(deck.pop())
            
        return list(queue)
     
