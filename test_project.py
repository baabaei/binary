# ---- Your Binary Search Function ----
def binary_search(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, x, low, mid - 1)
        else:
            return binary_search(array, x, mid + 1, high)
    return -1

# ---- Tester Function ----
def test_binary_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_values = [1, 5, 10, -1, 11, 7, 3]  # values to test
    print("Testing binary_search function:\n")

    for value in test_values:
        result = binary_search(array, value, 0, len(array) - 1)
        if result != -1:
            print(f"✅ Value {value} found at index {result}")
        else:
            print(f"❌ Value {value} not found in array")

# ---- Run Tester ----
test_binary_search()
