def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr

def selectionSortMain():
  print(selectionSort([5, 11, 6, 13, 9, 10, 2, 4, 10, 9, 13, 14, 23, 43, 19, 66, 46]))

