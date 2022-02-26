inpt =list(map(int,input().split(" ")))
no_prob = inpt[0]
travl_time = inpt[1]
 
availableTime  = 240-travl_time
solved = 0
 
left =0
right = no_prob
 
while left <= right:
   
   half = left + ( right-left)//2
   curTime = (half)*(2*5 + (half-1)*5)/2
   
   if curTime > availableTime:
      right = half -1
   elif curTime <= availableTime:
      solved = half
      left = half + 1
   
print(solved)