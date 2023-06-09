def count_elements_greater_than_neighbors(nums):
    count = 0

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            count += 1

    return count


# Example usage
numbers = [1, 5, 3, 7, 2, 8, 4]
result = count_elements_greater_than_neighbors(numbers)
print("Количество элементов больше, чем их соседей:", result)

