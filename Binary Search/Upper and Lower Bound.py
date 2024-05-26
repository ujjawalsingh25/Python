def lower_and_upper_bound():
    
    def lower_bound(arr, target):
        ans, n = len(arr), len(arr)         # n range from len(arr) t0 len(arr)
        low, high = 0, n-1                  # high range from 0 to n-1
        
        while low <= high:
            mid = low + (high - low) // 2;        
            if arr[mid] >= target:                 # for upper_bound, if(arr[mid] > target) 
                ans = mid                         # '>=' will be set to '>' only
                high = mid -1
            else:
                low = mid + 1;
        return ans;

    n = int(input("Enter Size: "))
    arr = list(map(int, input().split()))
    target = int(input("Enter Target: "))
    
    lb = lower_bound(arr, target)
    print(lb)
    
if __name__ == "__main__":
    lower_and_upper_bound()
    

    
