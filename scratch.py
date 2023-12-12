N = int(input())
ar = [0] * N
for i in range(N):
  ar[i] = int(input())
max_val = ar[0]
for i in range(1, N):
  max_val = max(max_val, ar[i])

print(max_val)


N = int(input())
ar = [[0] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    ar[i][j] = int(input())

for i in range(N):
  ar[i].sort()


# assume an O(1) swap(a, b) function that swaps the values a and b
N = int(input())
ar = [[0] * N] * N
for i in range(N):
  for j in range(N/2):
    swap(ar[i][j], ar[i][N - j])


# assume the log2(N) function takes O(1) time
# assume string concatenation takes O(1) time
def func(str, idx, len):
  if idx == len:
    print(str)
  else:
    func(str + "a", idx + 1, len)
    func(str + "b", idx + 1, len)
...
N = int(input())
func("", 0, int(log2(N)))


N = int(input())
bin = []
while N != 0:
  bin.append(N)
  N //= 2