'''
def binary_search_iterative():
    def binary_search(arr, target):
        low, high =0, len(arr)-1
    
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


    def array_input():
        n = int(input("Enter size: "))
        arr = list(map(int, input().split()))
        return arr

    arr = array_input()
    target = int(input("Enter target: "))
    
    result = binary_search(arr, target)
    print("Index :",result)

if __name__ == "__main__":
    binary_search_iterative()


'''

def binary_search_recursive():
    def binary_search(arr, low, high, target):
    
        mid = low + (high - low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            binary_search(arr, mid + 1, high, target)
        else:
            binary_search(arr, low, mid - 1, target)
        
    def array_input():
        n = int(input("Enter size: "))
        arr = list(map(int, input().split()))
        return arr

    arr = array_input()
    target = int(input("Enter target: "))
    
    result = binary_search(arr, 0, len(arr) - 1, target)
    print("Index :",result)

if __name__ == "__main__":
    binary_search_recursive()
