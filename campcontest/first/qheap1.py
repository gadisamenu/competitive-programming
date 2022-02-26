import heapq
heap = []
q = eval(input())
deleted = set()
while q:
    inp = list(map(int,input().split(" ")))
    
    if inp[0] == 1:
        if inp[1] in deleted:
            deleted.remove(inp[1])
        else:
            heapq.heappush(heap,inp[1])
            
    elif inp[0] == 2:
        if heap[0] == inp[1]:
            heapq.heappop(heap)
        else:
            deleted.add(inp[1])
        
    elif inp[0] == 3:
        while heap and heap[0] in deleted:
            deleted.remove(heapq.heappop(heap))
        if heap:
            print(heap[0])
        else:
            print()
    q-=1