# Lab 7 – Time and Space Complexity

## 1. find_max(arr)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Reason: The list is checked once to find the maximum element.

## 2. has_duplicate(arr)

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

Reason: Each element is compared with the other elements using nested loops.

## 3. sum_digits(n)

**Time Complexity:** O(log n)  
**Space Complexity:** O(log n)

Reason: The number is divided by 10 in every recursive call.

## 4. print_pairs(arr)

**Time Complexity:** O(n²)  
**Space Complexity:** O(n²)

Reason: All possible pairs are generated and stored in the result list.

## 5. binary_search(arr, target)

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

Reason: The search range becomes half after every iteration.

## 6. matrix_multiply(A, B)

**Time Complexity:** O(n³)  
**Space Complexity:** O(n²)

Reason: Three nested loops are used and an n × n result matrix is created.

## 7. to_sparse(matrix)

**Time Complexity:** O(m × n)  
**Space Complexity:** O(k)

Reason: Every matrix element is checked and only non-zero elements are stored.

## 8. process(n)

**Time Complexity:** O(n²)

Reason: The first loop takes O(n), while the nested loops take O(n²). The larger one is O(n²).

## 9. check_first_ten(arr)

**Time Complexity:** O(n)

Reason: The outer loop runs n times and the inner loop always runs only 10 times.

## 10. reverse_new(arr)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Reason: A new reversed list is created containing all elements.

## 11. reverse_in_place(arr)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Reason: The elements are swapped inside the same list without creating another list.

## 12. factorial(n)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Reason: The function calls itself n times and uses recursive call stack.

## 13. fibonacci(n)

**Time Complexity:** O(2^n)  
**Space Complexity:** O(n)

Reason: Each call creates two more recursive calls, so the number of calls grows very quickly.

## 14. count_pairs_with_sum(arr, target)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Reason: A set is used to store elements and set lookup takes O(1) on average.

## 15. print_all_subsets(arr)

**Time Complexity:** O(n × 2^n)

Reason: There are 2^n possible subsets and each subset takes up to n operations to check.

## 16. merge_sorted(a, b)

**Time Complexity:** O(m + n)  
**Space Complexity:** O(m + n)

Reason: Both lists are traversed once and a new result list is created.

## 17. is_palindrome(s)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Reason: The string is reversed using slicing, which creates a new string.

## 18. flatten(matrix)

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)

Reason: All elements of the matrix are visited and stored in a new list.

## 19. power(base, exp)

**Time Complexity:** O(exp)  
**Space Complexity:** O(exp)

Reason: The function makes one recursive call for each decrease of exp.

## 20. fast_power(base, exp)

**Time Complexity:** O(log exp)  
**Space Complexity:** O(log exp)

Reason: The exponent is divided by 2 in every recursive call.

## 21. has_common_element(a, b)

**Time Complexity:** O(n × m)  
**Space Complexity:** O(1)

Reason: Every element of one list may be compared with every element of the other list.

## 22. build_frequency_map(arr)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Reason: The list is traversed once and the frequency of each element is stored in a dictionary.