def _visit_range(start, stop, action):
    if start >= stop:
        return
    if stop - start == 1:
        action(start)
        return

    middle = (start + stop) // 2
    _visit_range(start, middle, action)
    _visit_range(middle, stop, action)


# 1. Максимальна кількість одиниць поспіль
def find_max_consecutive_ones(nums):
    current = 0
    longest = 0

    def inspect(index):
        nonlocal current, longest
        if nums[index] == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0

    _visit_range(0, len(nums), inspect)
    return longest


# 2. Кількість чисел із парною кількістю цифр
def find_numbers(nums):
    def count_digits(number):
        if number < 10:
            return 1
        return 1 + count_digits(number // 10)

    count = 0

    def inspect(index):
        nonlocal count
        if count_digits(nums[index]) % 2 == 0:
            count += 1

    _visit_range(0, len(nums), inspect)
    return count


# 3. Квадрати відсортованого масиву
def sorted_squares(nums):
    size = len(nums)
    result = [0] * size
    left = 0
    right = size - 1

    def place_square(position):
        nonlocal left, right
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]

        if left_square > right_square:
            result[size - 1 - position] = left_square
            left += 1
        else:
            result[size - 1 - position] = right_square
            right -= 1

    _visit_range(0, size, place_square)
    return result


# 4. Подвоєння нулів зі збереженням довжини початкового масиву
def duplicate_zeros(arr):
    size = len(arr)
    zero_count = 0

    def count_zero(index):
        nonlocal zero_count
        if arr[index] == 0:
            zero_count += 1

    _visit_range(0, size, count_zero)
    write = size + zero_count - 1

    def copy_backwards(offset):
        nonlocal write
        value = arr[size - 1 - offset]

        if write < size:
            arr[write] = value
        write -= 1

        if value == 0:
            if write < size:
                arr[write] = 0
            write -= 1

    _visit_range(0, size, copy_backwards)


# 5. Об'єднання двох відсортованих масивів
def merge(nums1, m, nums2, n):
    left = m - 1
    right = n - 1
    write = m + n - 1

    def place_largest(_):
        nonlocal left, right, write
        if right < 0:
            return

        if left >= 0 and nums1[left] > nums2[right]:
            nums1[write] = nums1[left]
            left -= 1
        else:
            nums1[write] = nums2[right]
            right -= 1
        write -= 1

    _visit_range(0, m + n, place_largest)


# 6. Видалення дублікатів із відсортованого масиву
def remove_duplicates(nums):
    if not nums:
        return 0

    unique_count = 1

    def inspect(index):
        nonlocal unique_count
        if nums[index] != nums[unique_count - 1]:
            nums[unique_count] = nums[index]
            unique_count += 1

    _visit_range(1, len(nums), inspect)
    return unique_count


# 7. Перевірка наявності числа та його подвійника.
def check_if_exist(arr):
    seen = set()
    found = False

    def inspect(index):
        nonlocal found
        if found:
            return

        value = arr[index]
        if value * 2 in seen or (value % 2 == 0 and value // 2 in seen):
            found = True

        seen.add(value)

    _visit_range(0, len(arr), inspect)
    return found


# 8. Перевірка гірського масиву
def valid_mountain_array(arr):
    if len(arr) < 3:
        return False

    descending = False
    valid = True

    def inspect(index):
        nonlocal descending, valid
        if not valid:
            return

        if arr[index] == arr[index - 1]:
            valid = False
        elif arr[index] > arr[index - 1]:
            if descending:
                valid = False
        else:
            if index == 1:
                valid = False
            descending = True

    _visit_range(1, len(arr), inspect)
    return valid and descending


# 9. Заміна елементів найбільшим значенням праворуч
def replace_elements(arr):
    largest = -1
    size = len(arr)

    def replace(offset):
        nonlocal largest
        index = size - 1 - offset
        original = arr[index]
        arr[index] = largest
        if original > largest:
            largest = original

    _visit_range(0, size, replace)
    return arr


# 10. Переміщення парних чисел перед непарними
def sort_array_by_parity(nums):
    even_count = 0

    def move_even(index):
        nonlocal even_count
        if nums[index] % 2 == 0:
            nums[even_count], nums[index] = nums[index], nums[even_count]
            even_count += 1

    _visit_range(0, len(nums), move_even)
    return nums


if __name__ == "__main__":
    print("1. Максимальна кількість одиниць поспіль:")
    print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
    print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))

    print("\n2. Числа з парною кількістю цифр:")
    print(find_numbers([12, 345, 2, 6, 7896]))
    print(find_numbers([555, 901, 482, 1771]))

    print("\n3. Квадрати відсортованого масиву:")
    print(sorted_squares([-4, -1, 0, 3, 10]))
    print(sorted_squares([-7, -3, 2, 3, 11]))

    print("\n4. Подвійні нулі:")
    zeros_first = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(zeros_first)
    print(zeros_first)
    zeros_second = [1, 2, 3]
    duplicate_zeros(zeros_second)
    print(zeros_second)

    print("\n5. Об'єднання відсортованих масивів:")
    merged_first = [1, 2, 3, 0, 0, 0]
    merge(merged_first, 3, [2, 5, 6], 3)
    print(merged_first)
    merged_second = [1]
    merge(merged_second, 1, [], 0)
    print(merged_second)
    merged_third = [0]
    merge(merged_third, 0, [1], 1)
    print(merged_third)

    print("\n6. Видалення дублікатів (k та перші k елементів):")
    duplicates_first = [1, 1, 2]
    k_first = remove_duplicates(duplicates_first)
    print(k_first, duplicates_first[:k_first])
    duplicates_second = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k_second = remove_duplicates(duplicates_second)
    print(k_second, duplicates_second[:k_second])

    print("\n7. Наявність числа та його подвійника:")
    print(check_if_exist([10, 2, 5, 3]))
    print(check_if_exist([3, 1, 7, 11]))

    print("\n8. Гірський масив:")
    print(valid_mountain_array([2, 1]))
    print(valid_mountain_array([3, 5, 5]))
    print(valid_mountain_array([0, 3, 2, 1]))

    print("\n9. Найбільший елемент праворуч:")
    print(replace_elements([17, 18, 5, 4, 6, 1]))
    print(replace_elements([400]))

    print("\n10. Парні числа перед непарними:")
    print(sort_array_by_parity([3, 1, 2, 4]))
    print(sort_array_by_parity([0]))
