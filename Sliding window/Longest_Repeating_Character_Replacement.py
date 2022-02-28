def characterReplacement(s,k):
        hash_map={}
        window_start=0
        max_so_far=0
        maxx_length=0
        for window_end in range(len(s)):
            current_char=s[window_end]
            hash_map[current_char]=hash_map.get(current_char,0)+1
            max_so_far=max(max_so_far,hash_map[current_char])
            if window_end-window_start+1-max_so_far>k:
                left_char=s[window_start]
                hash_map[left_char]-=1
                window_start+=1
            maxx_length=max(maxx_length,window_end-window_start+1)    
        return maxx_length             
                