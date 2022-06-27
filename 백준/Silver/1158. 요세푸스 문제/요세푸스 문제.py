import sys
from collections import deque

seq = sys.stdin.readline().split()
N = int(seq[0])
K = int(seq[1])

seq_queue = deque(range(1,N+1))
seq_list = []

for i in range(1, N*K+1):
    if i%K==0:
        seq_list.append(seq_queue.popleft())
    else:
        seq_queue.append(seq_queue.popleft())

print("<" + ", ".join(map(str, seq_list)) + ">")    # use map() to convert int list to str list
