def single_element_on_sorted_array():
    
    def single_sorted(arr):
        n = len(arr)
        low, high = 0, n - 1
        if n==1:
            return arr[0]
        elif arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
        
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
                return arr[mid]
            # In left half
            elif mid % 2 == 1 and arr[mid] == arr[mid-1] or mid % 2 == 0 and arr[mid] == arr[mid+1]:
                    low = mid+1
            # In right half
            else:
                high = mid-1
        
    
    n = int(input("Enter Size: "))
    arr = list(map(int,input().split()))
    element = single_sorted(arr)
    print("Single element in sorted array: ",element)
    
    
if __name__ == "__main__":
    single_element_on_sorted_array()
        
    