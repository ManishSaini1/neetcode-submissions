class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
   /**
 * @param {number[]} nums
 * @returns {number[]}
 */
 productExceptSelf(nums) {
    const n = nums.length;
    const output = new Array(n);

    // Step 1: Calculate prefix products
    // output[i] contains the product of all elements to the left of i
    output[0] = 1;
    for (let i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }

    // Step 2: Calculate suffix products on the fly and multiply
    // suffix tracks the product of all elements to the right of i
    let suffix = 1;
    for (let i = n - 1; i >= 0; i--) {
        output[i] = output[i] * suffix;
        suffix *= nums[i];
    }

    return output;
}

// Example usage:
// Output: [48, 24, 12, 8]
}
