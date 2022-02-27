class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        tot_weight = 0
        max_wght = weights[0]
        for weight in weights:
            max_wght = weight if weight > max_wght else max_wght
            tot_weight+= weight
        
        min_cap = 0
        max_cap = tot_weight
        
        my_capcty = tot_weight
        
        while min_cap <= max_cap:
            cap = min_cap + (max_cap - min_cap)//2
            if cap < max_wght:
                min_cap= cap+1
                continue
            
            n_days = 1
            per_day_wght= 0
            for weight in weights:
                per_day_wght+= weight
                if per_day_wght > cap:
                    n_days+=1
                    per_day_wght = weight
                    
            if n_days <= days:
                my_capcty = min(my_capcty,cap)
                max_cap = cap-1
            else:
                min_cap = cap+1
            
           
        return my_capcty
                
                    