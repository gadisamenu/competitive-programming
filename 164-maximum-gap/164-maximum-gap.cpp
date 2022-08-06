class Solution {
public:
    int maximumGap(vector<int>& nums) {
        set<int> s(nums.begin(),nums.end());
            
        int ans = 0;
            
        int pre = *s.begin();
            
        for (auto itr :s ){
            ans = max(ans,itr - pre);
            pre = itr;
        }
        
        return ans;
        
    }
};