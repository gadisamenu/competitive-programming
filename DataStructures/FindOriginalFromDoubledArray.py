class Solution:
    def findOriginalArray(self, changed):
        length = len(changed)
        if length %2 !=0:
            return []
        changed.sort()
        i = 0
        while i < length:
            if changed[i] != 0:
                break
            i +=1
        if i > 0 and i%2 != 0:
            return []
        org = [0]*(i//2)
        j = i+1
        while i <len(changed) and j < len(changed):
            if changed[j] < 0:
                j +=1
            elif (changed[i])*2 < changed[j]:
                if i == j:
                    i += 1
                    j +=1
                else:
                    i+=1
            elif changed[i]*2 == changed[j]:
                org.append(changed[i])
                changed[j] *=-1
                i += 1
                j += 1
            else:
                j +=1
      
        if len(org) != length/2:
            org =[]
        return org
                