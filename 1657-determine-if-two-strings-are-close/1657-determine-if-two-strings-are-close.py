class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        start_count = Counter(word1)
        target_count = Counter(word2)
        if len(start_count) != len(target_count):
            return False
        
        for to in target_count:
            for frm  in start_count:
                if frm == to:
                    if start_count[frm] == target_count[to]:
                        start_count.pop(frm)
                        break
                elif start_count[frm] == target_count[to] and to in start_count:
                    start_count[frm] = start_count[to]
                    start_count.pop(to)
                    break
                    
        for k in start_count:
            if start_count[k]!=0:
                return False
        return True

                    