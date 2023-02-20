class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # queryIP = queryIP.replace(".",":")
        ip = queryIP.split(".")
        if len(ip) == 4:
            valid = False
            for block in ip:
                if len(block) > 0 and  block.isdigit():
                    if block[0] != "0" or len(block) == 1:
                        _num = int(block)
                        if 0 <= _num <= 255:
                            valid = True
                if not valid:
                    return "Neither"
                valid = False
            return "IPv4"
        
        ip = queryIP.split(":")       
        if len(ip) == 8:
            valids= set()
            for i in range(10):
                valids.add(str(i))
            for i in range(97,103):
                ltr = chr(i)
                valids.add(ltr)
                valids.add(ltr.upper())
            for block in ip:
                if 4 < len(block) or len(block) == 0:
                    return "Neither"
                for _chr in block:
                    if _chr not in valids:
                        return "Neither"
                    
            return "IPv6"

        return "Neither"