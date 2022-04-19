class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_owner ={}
        def find_owner(email):
            if email == account_owner[email][0]:
                return account_owner[email]            
            account_owner[email] = find_owner(account_owner[email][0])
            return account_owner[email]
               
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in account_owner:
                    account_owner[find_owner(accounts[i][j])[0]] = account_owner[find_owner(accounts[i][1])[0]]
                else:
                    account_owner[accounts[i][j]] = [accounts[i][1],i]
                
        grouped = defaultdict(set)
        for email in account_owner:
            owner = find_owner(email)[0]
            grouped[owner].add(email)
        ans = []
        for p in grouped:
            ans.append([accounts[account_owner[p][1]][0]])
            ans[-1].extend(sorted(grouped[p]))
    
        return ans
                
                
            
            
            