
no_sh = int(input())
price_in_sh = list(map(int,input().split(" ")))
price_in_sh.sort()
lgth = len(price_in_sh)
 
no_days = int(input())
for n in range(no_days):
   my_mny = int(input())
   
   left =0
   right = lgth -1
   while left <= right:
      m = left + (right-left)//2
      
      if price_in_sh[m] < my_mny:
         left = m+1
      elif price_in_sh[m] > my_mny:
         right = m-1
      else:
         break
      
   if price_in_sh[m] > my_mny:
      print(m)
   else:
      print(m+1)
   
   