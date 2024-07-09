def merge_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Append remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# Test cases
print(merge_sorted_lists([1, 2, 5, 6, 8], [3, 4, 10]))  # Expected: [1, 2, 3, 4, 5, 6, 8, 10]
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Expected: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([], [1, 2, 3]))  # Expected: [1, 2, 3]
print(merge_sorted_lists([1, 2, 3], []))  # Expected: [1, 2, 3]
print(merge_sorted_lists([1, 1, 1], [1, 1, 1]))  # Expected: [1, 1, 1, 1, 1, 1]