n_sushi = int (input())
t_sushies = list(map(int,input().split(" ")))
 
my_sushi=0
 
srt = 0
mdl = 0 
end = 0
 
while end < n_sushi:
   
   if t_sushies[srt] == t_sushies[mdl]==t_sushies[end]:
      mdl +=1
      end +=1
   elif t_sushies[mdl] == t_sushies[end]:
      
      end +=1
   else:
      my_sushi = max(my_sushi,2*(min(mdl-srt,end-mdl)))
      srt = mdl
      mdl = end
   
my_sushi = max(my_sushi,2*(min(mdl-srt,end-mdl)))
      
print(my_sushi)