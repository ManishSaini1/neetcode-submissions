class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxLength = 0;
        let left = 0;
        const seen = new Set();

        for (let right = 0; right < s.length; right++) {
            const char = s[right];

            // Shrink window from the left until the duplicate character is removed
            while (seen.has(char)) {
                seen.delete(s[left]);
                left++;
            }

            seen.add(char);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}