class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)
        
        for path in paths:
            l_path = path.split(" ")
            for i in range(1,len(l_path)):
                fname_cont = l_path[i].split("(")
                duplicates[fname_cont[1]].append(l_path[0]+"/"+fname_cont[0])
                
        return filter(lambda x: len(x) > 1, duplicates.values())
                