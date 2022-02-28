def lengthOfLongestSubstring(s):
        hash_map=dict()
        window_start=0
        max_length=0
        for window_end in range(len(s)):
            current_char=s[window_end]
            if current_char in hash_map:
                window_start=max(window_start,hash_map[current_char]+1)
            max_length=max(max_length,window_end-window_start+1)
            hash_map[current_char]=window_end        
        return max_length 