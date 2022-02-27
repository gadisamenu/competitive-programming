class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lgth = len(citations)
        
        h_ind = 0
        
        left =0
        right= citations[-1]
        
        while left <=right:
            
            try_citation = left + (right-left)//2
            
            c_left = 0
            c_right= lgth -1
            ind= None
            while c_left <= c_right:
                idx = c_left + (c_right - c_left)//2
                
                if citations[idx] < try_citation:
                    c_left = idx +1
                    
                elif citations[idx] > try_citation:
                    c_right = idx -1
                else:
                    ind = idx
                    c_right = idx -1
                    
            if ind == None:
                ind = idx if citations[idx] > try_citation else idx+1
                
             
    
            if try_citation <= lgth - ind:
                h_ind = max(h_ind,try_citation)
                left = try_citation +1
            else:
                right = try_citation -1

                
        return h_ind
