class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
 
    int _min = 1;
        
    set<int>  s(nums.begin(),nums.end());
 
    for (int const &c: s) {
        
        if (c > 0){
            if ( _min == c){
                _min++;
            }
            else{
                break;
            }
        }
    }
        
   
    return  _min;

    }
};