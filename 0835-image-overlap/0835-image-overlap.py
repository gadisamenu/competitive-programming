class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        answer = 0
        if self.check(img1) and self.check(img2):
            lgth = len(img1)
            start =lgth-1

            for row in range(-start,lgth):
                for col in range(-start,lgth):
                    answer = max(self.count_match(img1,img2,row,col),answer)
        return answer
    
    def check(self,img):
        for rw in img:
            for cell in rw:
                if cell:
                    return True
        
    
    def count_match(self,img1,img2,rof,cof):
        start_r,end_r = (rof,len(img1)) if rof > 0 else (0,len(img1)+rof)
        start_c,end_c = (cof,len(img1)) if cof > 0 else (0,len(img1)+cof)

        
        count =0
        for row in range(start_r,end_r):
            for col in range(start_c,end_c):
                if img1[row-rof][col-cof] and img2[row][col]:
                    count += 1
        return count
                

