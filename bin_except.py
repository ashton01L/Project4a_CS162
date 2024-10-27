# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Modify the binary search function from the exploration so that, instead of returning -1 when the target
# value is not in the list, raises a TargetNotFound exception (you'll need to define this exception class).
# Otherwise it should function normally.
class TargetNotFound(Exception):
  """
  Exception raised when the search on a_list does not find a target value.
  """


def binary_search(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns custom TargetNotFound exception, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle  # Return the index of the found target
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound(f"Value '{target}' not found in the list.")

# try:
#     index = binary_search([1, 3, 5, 7, 9], 4)
#     print(f"Target found at index: {index}")
# except TargetNotFound as e:
#     print(e)