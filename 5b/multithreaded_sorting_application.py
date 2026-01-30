import threading

# This is our global data
arr = [38, 27, 43, 3, 9, 82, 10, 5]
n = len(arr)

# This is the econd global array for merged result
merged_arr = [0] * n


# I used simple bubble sorting function as it is quite easy.
def sort_sublist(start, end):

    
    for i in range(start, end + 1):
        for j in range(start, end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# This is where we merge the two sorted halves of arr
def merge_sublists(mid):

    i = 0           
    j = mid + 1     
    k = 0           

    # Merging while both halves have elements
    while i <= mid and j < n:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
        k += 1

    # Copying the remaining elements from left half
    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1

    # Copying the remaining elements from right half
    while j < n:
        merged_arr[k] = arr[j]
        j += 1
        k += 1


# Main Parent thread
if __name__ == "__main__":
    print("Original array:", arr)

    mid = n // 2 - 1

    # Creating sorting threads
    t1 = threading.Thread(target=sort_sublist, args=(0, mid))
    t2 = threading.Thread(target=sort_sublist, args=(mid + 1, n - 1))

    # Start sorting threads
    t1.start()
    t2.start()

    # Wait for both sorting threads to finish
    t1.join()
    t2.join()

    print("After sorting sublists:", arr)

    

    # Create and start merging thread
    t3 = threading.Thread(target=merge_sublists, args=(mid,))
    t3.start()
    t3.join()

    print("Final sorted array:", merged_arr)


# My strategy to solve this problem:

# We divide the array into two halves and sort each half using two separate threads. Since threads share global memory, 
# both threads directly modify the same array but in different index ranges. After both sorting threads finish, 
# a third thread merges the two sorted halves into another global array. The parent thread waits for all threads using join() 
# and then prints the final sorted result.”

