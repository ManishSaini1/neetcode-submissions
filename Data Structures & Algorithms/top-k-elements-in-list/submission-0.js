class Solution {
  topKFrequent(nums, k) {
    const map = new Map();

    // 1. Build frequency map
    for (const num of nums) {
      map.set(num, (map.get(num) || 0) + 1);
    }

    // 2. Convert to array [[num, freq], ...] and sort by freq descending
    const sorted = Array.from(map.entries()).sort((a, b) => b[1] - a[1]);

    // 3. Extract the top k elements
    return sorted.slice(0, k).map(entry => entry[0]);
  }
}