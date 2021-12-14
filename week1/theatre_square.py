l,w,a=list(map(int,input().split()))
row = l//a
if l%a != 0:
    row +=1
col = w //a
if w % a != 0:
    col +=1
num_dominos = row * col
print(num_dominos)