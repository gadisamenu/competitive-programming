import math
tests = int (input())
 
for n in range(tests):
   goal = int(input())
   
   base = math.sqrt(goal)
   
   if math.floor(base) * math.floor(base) >= goal:
      print((math.floor(base)-1)*2)
      
   elif math.floor(base)* math.ceil(base) >= goal:
      print((math.floor(base)-1) + (math.ceil(base)-1))
   else:
      print((math.ceil(base)-1)*2)
   