class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    /**
 * @param {number[]} nums
 * @return {number[][]}
 */
 threeSum(nums) {
    const result = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        // If the current number is greater than 0, remaining sum can't be 0
        if (nums[i] > 0) break;

        // Skip duplicates for the first element
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                // Skip duplicates for the second element
                while (left < right && nums[left] === nums[left + 1]) left++;
                // Skip duplicates for the third element
                while (left < right && nums[right] === nums[right - 1]) right--;

                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return result;
};
}
