
def repeatedString(s, n):
    count = []
    times =1
    if n >= len(s):
        times = n//len(s)
        over = n - times* len(s)
        for id in range(len(s)):
            if s[id] == 'a':
                count.append(id)
    else:
        for id in range(n):
            if s[id] == 'a':
                count.append(id)
        return len(count)
    if n == times*len(s):
        return len(count)*times
    else:
        add =0
        for nu in count:
            if nu < over:
                add+=1
        return len(count)*times + add