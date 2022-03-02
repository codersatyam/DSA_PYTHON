def longestKSubstr(s, k):
        hash_map={}
        window_start=0
        maxx_length=0
        for window_end in range(len(s)):
            current_char=s[window_end]
            hash_map[current_char]=hash_map.get(current_char,0)+1
            if len(hash_map)>k:
                while len(hash_map)!=k:
                    left_char=s[window_start]
                    hash_map[left_char]-=1
                    if hash_map[left_char]==0:
                        del hash_map[left_char]
                    window_start+=1
            maxx_length=max(maxx_length,window_end-window_start+1)        
        if len(set(s))<k:
            return -1
        else:    
            return maxx_length     