import sys
def binary_s(key,arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + (high - low)//2)
        if arr[mid] == key:
            print(f"{key} found at index {mid}")
            return
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f"{key} not found ")

n = len(sys.argv) - 1
input_list = list(map(int,sys.argv[1:n]))
binary_s(int(sys.argv[n]),input_list)