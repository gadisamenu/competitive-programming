class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int,version1.split(".")))
        version2 = list(map(int,version2.split(".")))
        lgth = min(len(version1),len(version2))
        print(version1,version2)
        for v1,v2 in zip(version1[:lgth],version2[:lgth]):
            if v1 > v2 : return 1
            elif v1 < v2: return -1
                 
        if len(version1) > len(version2):
            for v1 in version1[lgth:]:
                if v1: return 1
        elif len(version1) < len(version2):
            for v2 in version2[lgth:]:
                if v2:return -1
        return 0
            
            