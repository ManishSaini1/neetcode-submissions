class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0;

        const set = new Set(nums);
        let maxStreak = 0;

        for (const num of set) {
            // Only start counting if 'num' is the sequence root
            if (!set.has(num - 1)) {
                let currentNum = num;
                let currentStreak = 1;

                while (set.has(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                if (currentStreak > maxStreak) {
                    maxStreak = currentStreak;
                }
            }
        }

        return maxStreak;
    }
}