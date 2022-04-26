tests= int(input())

for test in range(tests):
   n,k = tuple(map(int,input().split(" ")))
   required_ram = list(map(int,input().split(" ")))
   increases =list(map(int, input().split(" ")))
   paired = list(zip(required_ram, increases))
   paired.sort()
   
   for pair in paired:
      if pair[0] <=k:
         k+=pair[1]
      else:
         break
   print(k)
