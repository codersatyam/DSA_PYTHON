def minWindow(s,t):
        hash_map={}
        for char in t:
            hash_map[char]=hash_map.get(char,0)+1
        window_start=0
        count=len(hash_map)
        ans=""
        for window_end in range(len(s)):
            current_char=s[window_end]
            if current_char in hash_map:
                hash_map[current_char]-=1
                if hash_map[current_char]==0:
                    count-=1
            while count==0:
                if not ans or len(ans)>window_end-window_start+1:
                    ans=s[window_start:window_end+1]
                else:        
                    left_char=s[window_start]    
                    if left_char in hash_map:
                        hash_map[left_char]+=1
                        if hash_map[left_char]==1:
                            count+=1
                    window_start+=1   
        if len(t)>len(s):
            return ""
        else:
            return ans