class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMappings;
        numMappings.reserve(nums.size());
        
        // O(n)
        for (int i = 0; i < nums.size(); ++i)
            numMappings[nums[i]] = i;
        
        // O(n)
        for (int i = 0; i < nums.size(); ++i) {
            
            // O(1)
            const auto& counterPart = numMappings.find(target - nums[i]);
            if (counterPart != numMappings.end() && counterPart->second != i) {
                return { i, counterPart->second };
            }
        }
        
        return { -1, -1 };
    }
};

/*
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        vector<pair<int, int>> numEntries;
        numEntries.reserve(nums.size());
        
        // O(n)
        transform(nums.begin(), nums.end(), back_inserter(numEntries), [i = 0] (const int& num) mutable {
            return std::make_pair(i++, num);
        });
        
        // O(n log n)
        sort(numEntries.begin(), numEntries.end(), [] (const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        // O(n)
        while (left < right) {
            if (numEntries[left].second + numEntries[right].second < target) {
                ++left;
            } else if (numEntries[left].second + numEntries[right].second > target) {
                --right;
            } else {
                break;
            }
        }
        
        return { numEntries[left].first, numEntries[right].first };
    }
};
*/
