class Solution {
public:
    bool isAnagram(string s, string t) {
        std::string first = s;
        std::string second = t;

        std::sort(first.begin(), first.end());
        std::sort(second.begin(), second.end());

        if(first == second){
            return true;
        }
        else{
            return false;
        }
    }
};
