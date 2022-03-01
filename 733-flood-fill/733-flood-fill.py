class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        to_be_changed = image[sr][sc]
        
        if to_be_changed == newColor:
            return image
        
        row = len(image)
        col = len(image[0])
        
        
        
        
        
        def changer(r,c):
            image[r][c]= newColor
            
            
            if r-1 >= 0 and  image[r-1][c] == to_be_changed:
                changer(r-1,c)
                
            if r+1 < row and image[r+1][c] == to_be_changed:
                changer(r+1,c)
                
            if  c-1 >= 0 and image[r][c-1] == to_be_changed:
                changer(r,c-1)
                
            if  c+1 < col and image[r][c+1] == to_be_changed:
                changer(r,c+1)
                
        changer(sr,sc)
        
        return image