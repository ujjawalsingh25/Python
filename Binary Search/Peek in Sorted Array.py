def peek_in_sorted_array():
    
    def peek_in_sorted(arr):
        n = len(arr)
        low, high = 1, n-2
        if n == 1:
            return 0
        elif(arr[0] > arr[1]):
            return 0
        elif(arr[n-1] > arr[n-2]):
            return n-1
        
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
    
    n = int(input("Enter Size : "))
    arr = list(map(int,input().split()))
    element_index = peek_in_sorted(arr)
    print("Index position of peek element : ",element_index)

if __name__ == "__main__":
    peek_in_sorted_array()    
    
    
  