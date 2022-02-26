tests = int(input())
 
for n in range(tests):
   line1 = list(map(int,input().split(" ")))
   line2 = list(map(int,input().split(" ")))
   
   left = 1
   right = line1[1]
   
   gab= []
   i = 0
   K = line1[1]
   while i < line1[0]-1:
      gab.append(line2[i+1]-line2[i])
      i+=1
      
      
      
   while left <= right:
      k = left + (right -left)//2
      sum = k
      for g in gab:
         sum += min(g,k)
      
      if  sum > line1[1]:
         right = k-1
         K = k
      elif sum < line1[1]:
         left = k+ 1
      else:
         K = k
         break
   
   print(K)