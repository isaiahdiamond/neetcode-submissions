class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> idx_val;

        for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    idx_val.push_back(i);
                    idx_val.push_back(j);
                }
            }
        }
        return idx_val;
    }
};
