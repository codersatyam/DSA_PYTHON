def maximumSumSubarray (K,Arr):
        window_start=0
        current_window=0
        maxx_sum=0
        for window_end in range(len(Arr)):
            current_window+=Arr[window_end]
            if window_end-window_start+1==K:
                maxx_sum=max(maxx_sum,current_window)
                current_window-=Arr[window_start]
                window_start+=1
        return maxx_sum