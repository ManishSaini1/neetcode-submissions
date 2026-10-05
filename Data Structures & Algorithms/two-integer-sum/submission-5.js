class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {}; // Stores: { value: original_index }

        for (let i = 0; i < nums.length; i++) {
            const complement = target - nums[i];

            // If the complement exists in our map, we found our pair!
            if (map[complement] !== undefined) {
                // Return the smaller index first
                return [map[complement], i];
            }

            // Otherwise, store the current number and its index
            map[nums[i]] = i;
        }

        return [];
    }
}