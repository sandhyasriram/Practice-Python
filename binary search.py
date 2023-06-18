
position = -1

def search(list, element):

    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        mid_value = (lower + upper) // 2

        if list[mid_value] == element:  # here index of mid
            globals() ["position"] = mid_value
            return True
# if the mid_value and search value is both are same, it gives position and serch value.
# otherwise we can change the lower bound and upper bound
# if mid_value is lesser than search element, the mid_value become lower bound
# else mid_value is grater then search element, the mid_value become upperbound

        else:
            if list[mid_value] < element:
                lower = mid_value

            else:
                upper = mid_value
    return False

list = [4, 12, 34, 45, 89, 102]
element = 45

if search(list, element):
    print("found at", position)

else:
    print("not found")



# binary search by using for loop

pos = -1

def binary_search(list, n):

    l = 0
    u = len(list)-1

    for i in range(u + 1):
        mid = (l + u)//2
        if list[mid] == n:
            globals() ["pos"] = mid
            return mid

        else:
            if list[mid] < n:
                l = mid +1

            else:
                u = mid -1

    return -1

shorted_list = [34, 56, 89, 90, 102, 556, 70892, 895689]
n = 56

if binary_search(shorted_list, n):
    print("Found at", pos)

else:
    print("Not Found")


####

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    for _ in range(high + 1):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Example usage
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_element = 23
result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print("Element not found.")
