class Solution:
    def minimumOperations(self, nums: List[int]) -> int:        
        if len(nums) ==1:
            return 0

        evens =defaultdict(int)
        odds =defaultdict(int)
        ind =0
        while ind < len(nums):
            evens[nums[ind]]+=1
            if ind+1 < len(nums): odds[nums[ind+1]]+=1
            ind+=2
     
        ev = max(evens,key= lambda x: evens[x])
        od = max(odds,key=lambda x: odds[x])
               
        if ev != od:
            return len(nums)- evens[ev] - odds[od]
        elif len(evens) == 1 and len(odds) ==1:
            return len(nums)- evens[ev] if evens[ev] > odds[od] else len(nums)-odds[od]
        elif len(evens) == 1:
            odds.pop(od)
            return len(nums) - evens[ev] - odds[max(odds,key=lambda x: odds[x])]
        elif len(odds) == 1:
            evens.pop(ev)
            return len(nums) - odds[od]- evens[max(evens,key=lambda x: evens[x])]
        else:
            keep_ev= evens[ev]
            keep_od = odds[od]
            evens.pop(ev)
            odds.pop(od)
            return len(nums)- max(keep_ev + odds[max(odds,key=lambda x: odds[x])],keep_od + evens[max(evens,key=lambda x: evens[x])])
        
            