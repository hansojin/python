def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  global count, result
  tmp = []
  i = p
  j = q+1

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp.append(A[i])
      i += 1
    else:
      tmp.append(A[j])
      j += 1

  while i <= q:
    tmp.append(A[i])
    i += 1

  while j <= r:
    tmp.append(A[j])
    j += 1

  i = p
  t = 0
  
  while i <= r:
    A[i] = tmp[t]
    count += 1
    if count == k:
      result = A[i]
    else:
      i += 1
      t += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = -1
merge_sort(arr, 0, n-1)
print(result)
