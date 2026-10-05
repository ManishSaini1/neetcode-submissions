class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case check
        if not s or not t or len(s) < len(t):
            return ""

        # Using a 128-element array instead of a dictionary for ASCII characters.
        # This completely eliminates dictionary hashing overhead.
        char_map = [0] * 128 
        for char in t:
            char_map[ord(char)] += 1
            
        required = len(t)
        left = 0
        min_len = float('inf')
        start_idx = 0
        
        for right in range(len(s)):
            # Convert character to its ASCII integer index
            char_idx = ord(s[right])
            
            # If the value is > 0, it's a character we actively need
            if char_map[char_idx] > 0:
                required -= 1
                
            # Decrement the count (unneeded chars will just go negative)
            char_map[char_idx] -= 1
            
            # When we have found all required characters
            while required == 0:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start_idx = left
                
                # Try shrinking from the left
                left_char_idx = ord(s[left])
                char_map[left_char_idx] += 1
                
                # If restoring this character pushes its requirement above 0,
                # we broke the valid window
                if char_map[left_char_idx] > 0:
                    required += 1
                    
                left += 1
                
        return s[start_idx : start_idx + min_len] if min_len != float('inf') else ""