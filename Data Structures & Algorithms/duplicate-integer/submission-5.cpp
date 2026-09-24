class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int s = nums.size();
        std::unordered_set<int> no_dups;

        for(int i = 0; i < s; i++){
            no_dups.insert(nums[i]);
        }

        if(s == no_dups.size()){
            return false;
        }
        else{
            return true;
        }
    }
};