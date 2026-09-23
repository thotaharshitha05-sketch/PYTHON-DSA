def max_sum_subarray(arr, k):
  window_sum = sum(arr[:k])
  max_sum = window_sum
  for i in range(k, len(arr)):
      window_sum = window_sum - arr[i - k] + arr[i]
      max_sum = max(max_sum, window_sum)
  return max_sum
temperatures = [2, 1, 5, 1, 3, 2, 8, 1, 3]
print(max_sum_subarray(temperatures, 3))