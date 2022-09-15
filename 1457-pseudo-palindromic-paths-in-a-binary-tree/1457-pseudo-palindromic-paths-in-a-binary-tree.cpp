/**
 * Definition for a binary tree curr.first.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {        
        stack<pair<TreeNode*,int>> st;      
        st.push({root,0});
        int count = 0;
               
        while (!st.empty()){
            pair<TreeNode*,int> curr =  st.top();
            st.pop();
            if (curr.first != nullptr){
                curr.second =  curr.second ^ (1 << curr.first->val);
                if (curr.first->left == nullptr && curr.first->right == nullptr){
                    if ((curr.second & (curr.second - 1)) == 0){
                        count++;
                    }
                }
                else{
                    st.push({curr.first->right,curr.second});
                    st.push({curr.first->left,curr.second});
                }
            }
        }
        return count;
        
    }
};