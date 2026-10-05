class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        
        const count = {};
        
        // Track the net frequency difference
        for (let i = 0; i < s.length; i++) {
            const charS = s.charAt(i);
            const charT = t.charAt(i);
            
            count[charS] = (count[charS] || 0) + 1; // +1 for s
            count[charT] = (count[charT] || 0) - 1; // -1 for t
        }
        
        // If it's an anagram, every key must be exactly 0
        for (const key in count) {
            if (count[key] !== 0) {
                return false;
            }
        }
        
        return true;
    }
}